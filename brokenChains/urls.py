from django.urls import path
from . import views



urlpatterns = [
	path('habits/', views.HabitList.as_view(), name='habits-list'),
	path('habits/<int:pk>/', views.HabitDetail.as_view(), name='habit-detail'),
	path('sessions/', views.SessionList.as_view(), name='sessions-list'),
	path('sessions/<int:pk>/', views.SessionDetail.as_view(), name='session-detail'),
	path('users/signup/', views.UserRegistration.as_view(), name='user-registration'),
]