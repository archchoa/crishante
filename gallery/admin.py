from django.contrib import admin

from adminsortable.admin import SortableAdmin
from adminsortable.admin import SortableTabularInline

from .models import Photo
from .models import Section
from .models import Subsection
from .models import SubsectionPhoto


class PhotoInline(SortableTabularInline):
    model = Photo


class SubsectionPhotoInline(SortableTabularInline):
    model = SubsectionPhoto


class SectionAdmin(SortableAdmin):
    inlines = [
        PhotoInline,
    ]
    list_display = ('title', 'slug', 'description')


class SubsectionAdmin(SortableAdmin):
    inlines = [
        SubsectionPhotoInline,
    ]
    list_display = ('title', 'slug', 'description')


admin.site.register(Section, SectionAdmin)
admin.site.register(Subsection, SubsectionAdmin)
