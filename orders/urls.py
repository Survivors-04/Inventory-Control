from django.urls import path
from .views import OrderView


urlpatterns = [
    path('orders/', OrderView.as_view()),
    path('orders/<str:pk>/', OrderView.as_view()),
]