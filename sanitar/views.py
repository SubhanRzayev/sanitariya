from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from product.models import Category, Product
from services.models import Services
from services.views import *
from core.views import *
from core.models import *
from .models import *


# Create your views here.

class IndexView(ListView):
    model = Category
    template_name = 'index.html'
    success_url = reverse_lazy('sanitar:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_list"] = Product.objects.filter(is_published=True)[:4]
        context['services_list'] = Services.objects.filter(is_published = True)[:4]
        return context

class AboutView(ListView):
    model = Category
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_list"] = About.objects.all()
        return context
    