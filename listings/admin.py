from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_per_page = 25
    search_fields = ('title', 'description', 'address', 'city', 'state', 'price', 'zipcode')

admin.site.register(Listing, ListingAdmin)
