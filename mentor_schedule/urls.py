from django.urls import path
from . import views

urlpatterns = [
    path('', views.MentorScheduleView.as_view()),
    path('<str:pk>', views.mentorScheduleByIdView)
]
