from django.urls import path
from . import views

urlpatterns = [
  path('', views.MentorView.as_view()),
  path('filter', views.filterMentorView)
]
