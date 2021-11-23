from django.shortcuts import get_object_or_404, render
from product.models import Category, Product
from django.urls.base import reverse, reverse_lazy

from django.views.generic import ListView,DetailView

# Create your views here.

class ProductView(ListView):
    model = Product
    template_name = 'products.html'
    



class ProductDetailView(DetailView):
    model = Product
    template_name = 'products-details.html'

    def get_success_url(self):
        return reverse("product:product_detail", kwargs={"pk": self.object.pk})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] =get_object_or_404(Product,pk = self.kwargs['pk'])
        # context["products"] = Product.objects.filter(pk=id).first()
        return context
 
    

