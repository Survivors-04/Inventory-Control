from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("accounts/", views.AccountView.as_view()),
    path("accounts/<int:pk>/", views.AccountDetailedView.as_view()),
    path("codes/<int:pk>/", views.CodeView.as_view()),
    path("accounts/login/", views.LoginView.as_view()),

]
