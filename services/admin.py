from services.models import Services
from modeltranslation.admin import TranslationAdmin
from django.contrib import admin

# Register your models here.

# @admin.register(Services)
# class ProductAdmin(admin.ModelAdmin):   
#     list_display = ('title','cover_image','is_published',)
#     list_filter = ('title','is_published')
#     search_fields = ('title',)
    
#     fieldsets = (
#         ('Information', {
#             'fields': ('title','cover_image','description','is_published', )
#         }),
#     )
class ServicesAdmin(TranslationAdmin):
    pass


admin.site.register(Services,ServicesAdmin)


