from django.db import models

# Create your models here.



class About(models.Model):
    
    # information
    title = models.CharField(max_length=40,blank=True, verbose_name="Başlıq")
    about_image = models.ImageField(upload_to = 'about_image', verbose_name="Şəkil")
    description = models.TextField(max_length=1000, verbose_name="Ətraflı məlumat")


    class Meta:
        verbose_name = "Haqqımızda"
        verbose_name_plural = "Haqqımızda"



    def __str__(self):
        return self.title

    
    
class Image(models.Model):
    image = models.ImageField(upload_to= 'team_image', verbose_name="Şəkil")


    
        
    
    
        