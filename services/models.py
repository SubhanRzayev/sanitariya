from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

from django.urls.base import reverse, reverse_lazy
from django.utils import timezone

# class Category(models.Model):
#     """
#     Category model's save all services catagories
#     """
#     #information
#     category = models.CharField(max_length=50,default="Office Cleaning")

#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'

#     def __str__(self):
#         return self.category

    
class Services(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlıq")
    description = models.CharField(max_length=1000, default="Write the text", verbose_name="Ətraflı məlumat")
    cover_image = models.ImageField(upload_to = 'media/services_image', verbose_name="Şəkil")
    is_published =models.BooleanField(default=False, verbose_name="Saytda göstərilir?")



    class Meta:
        verbose_name = "Xidmət"
        verbose_name_plural = "Xidmətlər"


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("services:services_detail", kwargs={"pk": self.pk})

    
    





    


    


