from django.contrib import admin

from .forms import PoisForm
from .models import Listing, Poi


class PoiAdmin(admin.ModelAdmin):
    form = PoisForm


# Models
admin.site.register(Listing)
admin.site.register(Poi, PoiAdmin)
