from django.urls import path
from .views import ProductView, ProductDetailView


urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<str:pk>/', ProductDetailView.as_view()),
]