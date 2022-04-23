from django.urls import path
from . import views

urlpatterns = [
  path('', views.MentorView.as_view()),
  path('<str:pk>', views.getMentorView),
  path('filter', views.filterMentorView),
]
