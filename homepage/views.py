from django.views.generic.base import TemplateView
from django.shortcuts import render

from portfolio.models import Portfolio

from .models import Slide
from .models import Testimonial


class HomepageView(TemplateView):
    template_name = 'homepage/home.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['slides'] = Slide.objects.all()
        ctx['portfolio'] = Portfolio.objects.all()
        ctx['testimonials'] = Testimonial.objects.all()
        return ctx
