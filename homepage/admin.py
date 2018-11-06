from django.contrib import admin

from adminsortable.admin import SortableAdmin

from .models import Slide
from .models import Testimonial


class SlideAdmin(SortableAdmin):
    list_display = ('image',)

admin.site.register(Slide, SlideAdmin)


class TestimonialAdmin(SortableAdmin):
    list_display = ('customer', 'text')

admin.site.register(Testimonial, TestimonialAdmin)
