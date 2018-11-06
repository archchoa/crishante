from django.contrib import admin

from adminsortable.admin import SortableAdmin
from adminsortable.admin import SortableTabularInline

from .models import Photo
from .models import Portfolio
from .models import Work


class PhotoInline(SortableTabularInline):
    model = Photo


class PortfolioAdmin(SortableAdmin):
    list_display = ('title', 'slug', 'description')


class WorkAdmin(SortableAdmin):
    inlines = [
        PhotoInline,
    ]
    list_display = ('header', 'subheader', 'title', 'description', 'portfolio')


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Work, WorkAdmin)
