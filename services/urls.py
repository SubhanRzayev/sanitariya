from django.urls import path
from services.views import ServiceView,ServiceDetailView

app_name = 'services'

urlpatterns = [
    path('service/',ServiceView.as_view(),name = 'service'),
    path('service-detail/<int:pk>/',ServiceDetailView.as_view(),name='services_detail')
]
