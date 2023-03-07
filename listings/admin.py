from django.contrib import admin

from .forms import ListingsForm
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    form = ListingsForm

# Register your models here.
admin.site.register(Listing, ListingAdmin)
