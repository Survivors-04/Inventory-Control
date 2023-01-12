from django.urls import path
from .views import OrderView, OrderDetailView, SendOrderView

urlpatterns = [
    path('orders/', OrderView.as_view()),
    path('orders/<str:pk>/', OrderDetailView.as_view()),
    path('orders/sendOrders/<str:pk>/', SendOrderView.as_view()),

]