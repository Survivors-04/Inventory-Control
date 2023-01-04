from django.urls import path
from .views import ProductView


urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<str:pk>', ProductView.as_view()),
    
]