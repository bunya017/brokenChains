from django.urls import path
from . import views



urlpatterns = [
	path('habits/', views.HabitList.as_view(), name='habits-list'),
	path('habits/<int:pk>/', views.HabitDetail.as_view(), name='habit-detail'),
	path('sessions/', views.SessionList.as_view(), name='sessions-list'),
]