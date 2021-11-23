from services.models import Services
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DetailView
from django.urls import reverse

# Create your views here.

class ServiceView(ListView):
    model = Services
    template_name = 'service.html'
    success_url = 'services_detail'


    
    


class ServiceDetailView(DetailView):
    model = Services
    template_name = 'services-details.html'


    def get_success_url(self):
        return reverse("services:services_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = get_object_or_404(Services, pk = self.kwargs['pk'])
        return context
    