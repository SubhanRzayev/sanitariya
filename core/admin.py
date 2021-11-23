from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from core.models import Blog,Contact,Information

# Register your models here.

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title','cover_image' ,'description', 'is_published', 'created_at', 'update_at',)
#     list_filter = ('title', 'is_published',)
#     search_fields = ('title',)

@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('address',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message',)
  
class BlogAdmin(TranslationAdmin):
    pass


admin.site.register(Blog,BlogAdmin)