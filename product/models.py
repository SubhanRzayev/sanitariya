from django.db import models
from django.urls import reverse_lazy


# Create your models here.

class Product(models.Model):
    """
    Product model's save all products main info
    """
    #information

    category = models.ManyToManyField('Category',db_index=True,default='Something',blank=True,related_name='product_categories')


    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000,default='Write your text')
    cover_image = models.ImageField(upload_to='product_cover_image')
    is_published = models.BooleanField(default=False,blank=True)

    #moderations
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse_lazy("product:product_detail", kwargs={
            "pk": self.pk
            })
    

class Category(models.Model):
    """
    Category model's save all products Catecogories. 
    """
    #relation
    

    #information
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'home_category_images',default='IMG.JPG',blank = True,null = True)
    is_published =models.BooleanField(default=False)

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse_lazy("product:product", kwargs={"pk": self.pk})
    