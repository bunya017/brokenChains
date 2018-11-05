from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions
from .models import Habit, Session
from .serializers import HabitSerializer, SessionSerializer
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


class HabitDetail(generics.RetrieveDestroyAPIView):
	queryset = Habit.objects.all()
	serializer_class = HabitSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	@method_decorator(ensure_csrf_cookie)
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class SessionList(generics.ListCreateAPIView):
	queryset = Session.objects.all()
	serializer_class = SessionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	@method_decorator(ensure_csrf_cookie)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)