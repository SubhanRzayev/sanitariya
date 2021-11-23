from modeltranslation.admin import TranslationAdmin
from product.models import  Product
from django.contrib import admin



# Register your models here.

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title','cover_image','is_published',)
#     list_filter = ('title','is_published')
#     search_fields = ('title',)

#     fieldsets = (
#         ('Information', {
#             'fields': ('title','cover_image','description','is_published','category' )
#         }),
#     )



# admin.site.register(Category,ProductAdmin)   
# 
class ProductAdmin(TranslationAdmin):
    pass


admin.site.register(Product,ProductAdmin)  


    