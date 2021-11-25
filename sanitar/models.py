from django.db import models

# Create your models here.



class About(models.Model):
    
    # information
    title = models.CharField(max_length=40,blank=True)
    about_image = models.ImageField(upload_to = 'about_image')
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
    
    
class Image(models.Model):
    image = models.ImageField(upload_to= 'team_image')
    
        
    
    
        