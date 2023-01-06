from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryView.as_view()),   
    path("categories/<str:pk>/", views.CategoryDetailView.as_view()),   
]