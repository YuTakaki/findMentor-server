from django.urls import path
from . import views

urlpatterns = [
    path('', views.getScheduleView),
    path('<str:id>', views.saveScheduleView),
]
