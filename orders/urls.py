from django.urls import path
from .views import OrderView, OrderDetailView

urlpatterns = [
    path('orders/', OrderView.as_view()),
    path('orders/<str:pk>/', OrderDetailView.as_view()),
]