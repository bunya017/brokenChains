from django.urls import path
from . import views



urlpatterns = [
	path('habits/', views.HabitList.as_view(), name='habits-list'),
]