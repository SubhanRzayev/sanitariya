from django.contrib import admin
from sanitar.models import *

# Register your models here.


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title','about_image','description',)
    
admin.site.register(Image)

