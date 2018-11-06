from django.contrib import admin

from .models import Slide
from .models import Testimonial


class SlideAdmin(admin.ModelAdmin):
    list_display = ('image',)

admin.site.register(Slide, SlideAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('customer', 'text')

admin.site.register(Testimonial, TestimonialAdmin)
