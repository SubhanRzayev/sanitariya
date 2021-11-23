from sanitar.views import IndexView,AboutView
from django.urls import path


app_name = 'sanitar'
urlpatterns = [
    path('',IndexView.as_view(),name = 'index'),
    path('about/',AboutView.as_view(),name = 'about'),


]