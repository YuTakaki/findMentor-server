from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('verify', views.VerifyTokenView.as_view()),
    path('additional', views.UserInformationView.as_view()),
    path('logout', views.logoutView)
]
