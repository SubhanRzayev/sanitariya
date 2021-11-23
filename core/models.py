from django.db import models
from django.urls.base import reverse
from django.utils import timezone

# Create your models here.

class Blog(models.Model):

    # information
    title = models.CharField(max_length=60)
    cover_image = models.ImageField(upload_to = "media/blog_cover_image")
    description = models.CharField(max_length=1000)
    is_published = models.BooleanField(default=False)


    # moderations

    created_at = models.DateTimeField(default = timezone.now)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('core:blog_detail',args=[self.pk])


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=80)
    message = models.TextField(max_length=1000)
    
    #moderations
    created_at = models.DateTimeField(auto_now=True,blank=True)
    
    def __str__(self):
        return self.name



class Information(models.Model):
    street = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField(default='+994 55 400 16 09',)

    def __str__(self):
        return self.street
    

