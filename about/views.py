from django.shortcuts import render
from django.views.generic import TemplateView

from utils.functions import chunks

from .models import TeamMember, Service


class AboutUsView(TemplateView):
    template_name = 'about/about_us.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        services = Service.objects.all()
        services = list(chunks(services, 3))

        context['members'] = TeamMember.objects.all()
        context['split_services'] = services

        return context
