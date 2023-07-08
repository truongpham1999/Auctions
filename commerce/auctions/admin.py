from django.contrib import admin
from .models import User, Listings, Category, Bids, Comments

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'date_joined')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')

class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'title', 'start_bid', 'owner', 'category')

class BidsAdmin(admin.ModelAdmin):
    list_display = ('id', 'bidder', 'get_listing_name', 'winner', 'bid', 'date')

    def get_listing_name(self, obj):
        return obj.listing.title
    get_listing_name.short_description = 'Listing Name'  # Sets column name in admin site

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'commenter', 'get_listing_name', 'date')

    def get_listing_name(self, obj):
        return obj.listing.title
    get_listing_name.short_description = 'Listing Name'  # Sets column name in admin site

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Listings, ListingsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Bids, BidsAdmin)
admin.site.register(Comments, CommentsAdmin)