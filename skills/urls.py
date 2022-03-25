from django.urls import path
from . import views
urlpatterns = [
  path('', views.UserSkillsView.as_view())
]