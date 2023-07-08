from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import Max

from .models import User, Listings, Category, Bids, Comments


def get_categories():
    # Get all category objects
    return Category.objects.all()


def index(request):
    # The index view displays active listings and categories
    return render(request, "auctions/index.html", {
        "active_lists": Listings.objects.filter(is_active=True),  # Fetch all active listings
        "categories": get_categories()  # Fetch all categories
    })


def closed_listings(request):
    # The closed_listings view displays inactive listings and categories
    return render(request, "auctions/closed_listings.html", {
        "closed_lists": Listings.objects.filter(is_active=False), 
        "categories": get_categories() 
    })


def category_filter(request):
    # The category_filter view displays 'active' listings in a selected category
    category_id = request.POST['category']  # Get selected category from form
    category = Category.objects.get(id=category_id)  # Fetch category object
    active_lists = Listings.objects.filter(is_active=True, category=category)  # Get active listings in selected category
    return render(request, "auctions/index.html", {
        "active_lists": active_lists,
        "categories": get_categories()
    })

def closed_category_filter(request):
    # The closed_category_filter view displays 'inactive' listings in a selected category
    category_id = request.POST['category']  # Get selected category from form
    category = Category.objects.get(id=category_id)  # Fetch category object
    closed_lists = Listings.objects.filter(is_active=False, category=category)  # Get inactive listings in selected category
    return render(request, "auctions/closed_listings.html", {
        "closed_lists": closed_lists,
        "categories": get_categories()
    })

def login_view(request):
    # The login_view handles user authentication
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)  # Check if the entered credentials are correct

        if user is not None:
            login(request, user)  # Login the user
            return HttpResponseRedirect(reverse("index"))  # Redirect to the homepage
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."  # Show error message
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))  # Redirect to the homepage after logout


def register(request):
    # The register view handles user registration
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            # If passwords do not match, return an error message
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)  # Try to create a new user
            user.save()
        except IntegrityError:
            # If the username is already taken, return an error message
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)  # Login the new user
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def list_creating(request):
    # The list_creating view handles creation of a new listing
    if request.method == "POST":
        new_listing = Listings(
            title=request.POST['title'], 
            description=request.POST['description'],
            start_bid=request.POST['start_bid'], 
            img_url=request.POST['img_url'],
            owner=request.user, 
            category=Category.objects.get(category_name=request.POST['category'])
        )
        new_listing.save()
        return HttpResponseRedirect(reverse("index"))  # Redirect to the homepage
    
    return render(request, "auctions/create.html", {
        "categories": get_categories() 
    })


def listing(request, listing_id):
    # The listing view displays a single listing with all related information
    listing = get_object_or_404(Listings, pk=listing_id)  # Fetch the requested listing object or return 404 if not found

    highest_bid = listing.bids.all().order_by('-bid').first()  # Get the highest bid for the listing
    listing.current_bid = highest_bid.bid if highest_bid else listing.start_bid  # Set the current bid as the highest bid or the starting bid if there are no bids
    listing.save()

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "watchlist_users": listing.watchlist.all(),  # Fetch all users who added the listing to their watchlist
        "user": request.user,  # Current user
        "comments": listing.comments.all(),  # Fetch all comments for the listing
        "bids": listing.bids.all(),  # Fetch all bids for the listing
        "highest_bid": highest_bid,  # Highest bid
    })


def watchlist(request):
    # The watchlist view displays all listings in the current user's watchlist
    return render(request, "auctions/watchlist.html", {
        "watchlists": request.user.watchlist.all()  # Fetch all listings in the user's watchlist
    })


def toggle_watchlist(request, listing_id):
    # The toggle_watchlist view adds or removes a listing from the current user's watchlist
    listing = get_object_or_404(Listings, pk=listing_id)
    user = request.user  # Current user

    if user in listing.watchlist.all():
        # If the user has already added the listing to their watchlist, remove it
        listing.watchlist.remove(user)
    else:
        # If the user has not added the listing to their watchlist, add it
        listing.watchlist.add(user)
        
    return HttpResponseRedirect(reverse("listing", args=(listing_id,)))


def add_bid(request, listing_id):
    # The add_bid view handles creation of a new bid
    listing = get_object_or_404(Listings, pk=listing_id) 
    new_bid = Bids(
        bid=request.POST['added_bid'], 
        bidder=request.user, 
        listing=listing
    )
    new_bid.save()
    return HttpResponseRedirect(reverse("listing", args=(listing_id,)))


def add_comment(request, listing_id):
    # The add_comment view handles creation of a new comment
    listing = get_object_or_404(Listings, pk=listing_id)
    new_comment = Comments(
        comment=request.POST['new_comment'], 
        commenter=request.user, 
        listing=listing
        )
    new_comment.save() 
    return HttpResponseRedirect(reverse("listing", args=(listing_id,)))

def close_listing(request, listing_id):
    # The close_listing view handles closing of a listing
    listing = get_object_or_404(Listings, pk=listing_id)
    listing.is_active = False  # Close the listing
    listing.save()

    highest_bid = listing.bids.aggregate(Max('bid')).get('bid__max')  # Get the highest bid value
    highest_bid_object = listing.bids.filter(bid=highest_bid).first()  # Fetch the bid object with the highest bid

    if highest_bid_object:
        # If there is a highest bid, mark it as the winning bid
        highest_bid_object.winner = True
        highest_bid_object.save()
    return HttpResponseRedirect(reverse("listing", args=(listing_id,)))