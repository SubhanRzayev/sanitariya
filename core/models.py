from django.db import models
from django.urls.base import reverse
from django.utils import timezone

# Create your models here.

class Blog(models.Model):

    # information
    title = models.CharField(max_length=60, verbose_name="Başlıq")
    cover_image = models.ImageField(upload_to = "media/blog_cover_image", verbose_name="Şəkil")
    description = models.CharField(max_length=1000, verbose_name="Ətraflı məlumat")
    is_published = models.BooleanField(default=False, verbose_name="Saytda göstərilir?")


    # moderations

    created_at = models.DateTimeField(default = timezone.now)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('core:blog_detail',args=[self.pk])



    class Meta:
        verbose_name = "Xəbər"
        verbose_name_plural = "Xəbərlər"




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=80)
    message = models.TextField(max_length=1000)
    
    #moderations
    created_at = models.DateTimeField(auto_now=True,blank=True)
    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Əlaqə mesajı"
        verbose_name_plural = "Əlaqə mesajları"



class Information(models.Model):
    street = models.CharField(max_length=100, verbose_name="Küçə")
    address = models.CharField(max_length=100, verbose_name="Ünvan")
    phone = models.IntegerField(default='+994 55 400 16 09', verbose_name="Telefon")

    def __str__(self):
        return self.street
    

    class Meta:
        verbose_name = "Əlaqə məlumatları"
        verbose_name_plural = "Əlaqə məlumatları"
