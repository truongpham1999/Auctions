from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("closed_listings", views.closed_listings, name="closed_listings"),
    path("list_creating", views.list_creating, name="create"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("category_filter", views.category_filter, name="category_filter"),
    path("closed_category_filter", views.closed_category_filter, name="closed_category_filter"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("toggle_watchlist/<int:listing_id>", views.toggle_watchlist, name="toggle_watchlist"),
    path("add_bid/<int:listing_id>", views.add_bid, name="add_bid"),
    path("add_comment/<int:listing_id>", views.add_comment, name="add_comment"),
    path("close_listing/<int:listing_id>", views.close_listing, name="close_listing"),
]
