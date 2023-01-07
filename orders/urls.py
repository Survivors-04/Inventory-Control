from django.urls import path
from .views import OrderManagerView, OrderUserView

urlpatterns = [
    path('orders/', OrderManagerView.as_view()),
    path('orders/<str:pk>/', OrderUserView.as_view()),
]