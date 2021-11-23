from django.urls.base import reverse_lazy
from core.forms import ContactForm
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DetailView,CreateView
from . models import Blog, Contact, Information
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class BlogView(ListView):
    model =  Blog
    template_name = 'blog.html'    
    success_url = 'blog-detail'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog-detail.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context


    def get_success_url(self):
        return reverse("core:blog_detail",kwargs={"pk":self.object.pk}) 


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy("core:contact")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['information_list'] = Information.objects.all()

        return context

    def form_valid(self, form):
        context = super().form_valid(form)
        form.save()
        return context




    # def get_context_data(self, **kwargs):
    #     # context = super().get_context_data(**kwargs)
    #     # context[""] = 
    #     # return context
    
    


    
