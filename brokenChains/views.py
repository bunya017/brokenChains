from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions
from .models import Habit, Session
from .serializers import HabitSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse






class HabitList(generics.ListCreateAPIView):
	queryset = Habit.objects.all()
	serializer_class = HabitSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	@method_decorator(ensure_csrf_cookie)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)








