from django.urls import path

from core.views import BlogView,BlogDetailView,ContactView


app_name = 'core'

urlpatterns = [
    path('blog/',BlogView.as_view(),name = 'blog'),
    path('contact/',ContactView.as_view(),name = 'contact'),
    path('blog-detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    
]
