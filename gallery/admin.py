from django.contrib import admin

from adminsortable.admin import SortableAdmin
from adminsortable.admin import SortableTabularInline

from .models import Photo
from .models import Section


class PhotoInline(SortableTabularInline):
    model = Photo


class SectionAdmin(SortableAdmin):
    inlines = [
        PhotoInline,
    ]
    list_display = ('title', 'slug', 'description')

admin.site.register(Section, SectionAdmin)
