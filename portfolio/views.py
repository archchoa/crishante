from django.views.generic.list import ListView
from django.shortcuts import render

from .models import Portfolio


class PortfolioListView(ListView):
    model = Portfolio
