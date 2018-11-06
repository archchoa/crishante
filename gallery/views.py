from django.views.generic.list import ListView
from django.shortcuts import render

from .models import Section


class GalleryListView(ListView):
    model = Section
