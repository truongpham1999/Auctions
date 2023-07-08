from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Category(models.Model):
    category_name = models.CharField(max_length=40)

    def __str__(self):
        return self.category_name

class Listings(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    start_bid = models.FloatField()
    current_bid = models.FloatField(blank=True, null=True)
    img_url = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='listings')
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name='watchlist')

    def __str__(self):
        return "title: " + self.title + "," \
               "start_bid: " + str(self.start_bid) + ","

class Bids(models.Model):
    bid = models.FloatField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='bids')
    winner = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "bid: " + str(self.bid) + "," \
                "bidder: " + self.bidder.username + "," \
                "listing: " + self.listing.title

class Comments(models.Model):
    comment = models.CharField(max_length=1000)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "commenter: " + self.commenter.username + "," \
                "listing: " + self.listing.title




