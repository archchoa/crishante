from django.contrib import admin

from .models import Photo
from .models import Section


class PhotoInline(admin.TabularInline):
    model = Photo


class SectionAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]
    list_display = ('title', 'slug', 'description')

admin.site.register(Section, SectionAdmin)
