from django.contrib import admin

from .models import Photo
from .models import Portfolio
from .models import Work


class PhotoInline(admin.TabularInline):
    model = Photo


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')


class WorkAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]
    list_display = ('header', 'subheader', 'title', 'description', 'portfolio')


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Work, WorkAdmin)
