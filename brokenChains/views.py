from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions, serializers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken as DRFObtainAuthToken
from rest_framework.response import Response
from .models import Habit, Session
from .serializers import HabitSerializer, SessionSerializer, UserSerializer
from .exceptions import UniqueTogetherValidationError



class HabitList(generics.ListCreateAPIView):
	queryset = Habit.objects.all()
	serializer_class = HabitSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	@method_decorator(ensure_csrf_cookie)
	def perform_create(self, serializer):
		data = serializer.validated_data
		name = data['name'].title()
		message = 'Oops! You have created a habit with this name: \'' + data['name'] + '\' already.'
		if Habit.objects.filter(owner=self.request.user, name=name).exists():
			raise UniqueTogetherValidationError(message, 'name', None)
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

	def perform_create(self, serializer):
		data = serializer.validated_data
		habit = data['habit']
		name = habit.name +' - '+ data['name'].title()
		message = 'Oops! You have created a session with this name: \'' + data['name'] + '\' already.'
		if Session.objects.filter(habit=habit, name=name).exists():
			raise UniqueTogetherValidationError(message, 'name', None)
		serializer.save()

	@method_decorator(ensure_csrf_cookie)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class SessionDetail(generics.RetrieveDestroyAPIView):
	queryset = Session.objects.all()
	serializer_class = SessionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	@method_decorator(ensure_csrf_cookie)
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class ObtainAuthToken(DRFObtainAuthToken):

	@method_decorator(ensure_csrf_cookie)
	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data,
										   context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		return Response({'token': token.key})