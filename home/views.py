from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePage(TemplateView):
    """
    Displays HomePage"
    """
    template_name = "home/index.html"
