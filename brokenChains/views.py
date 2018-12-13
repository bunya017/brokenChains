from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions, serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken as DRFObtainAuthToken
from rest_framework.exceptions import APIException, NotAuthenticated, PermissionDenied
from rest_framework.response import Response
from .models import Habit, Session
from .serializers import HabitSerializer, SessionSerializer, UserSerializer



class HabitList(generics.ListCreateAPIView):
	serializer_class = HabitSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		try:
			queryset = Habit.objects.all().filter(owner=self.request.user)
		except TypeError:
			raise NotAuthenticated
		else:
			return queryset

	def perform_create(self, serializer):
		data = serializer.validated_data
		name = data['name'].title()
		detail = 'Oops! You have created a habit with this name: \'' + data['name'] + '\' already.'
		if Habit.objects.filter(owner=self.request.user, name=name).exists():
			raise PermissionDenied(detail=detail)
		serializer.save(owner=self.request.user)

	@method_decorator(ensure_csrf_cookie)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class HabitDetail(generics.RetrieveDestroyAPIView):
	serializer_class = HabitSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		try:
			queryset = Habit.objects.all().filter(owner=self.request.user)
		except TypeError:
			raise NotAuthenticated
		else:
			return queryset

	@method_decorator(ensure_csrf_cookie)
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class SessionList(generics.ListCreateAPIView):
	serializer_class = SessionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		try:
			queryset = Session.objects.all().filter(habit__owner=self.request.user)
		except TypeError:
			raise NotAuthenticated
		else:
			return queryset

	@method_decorator(ensure_csrf_cookie)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class SessionDetail(generics.RetrieveDestroyAPIView):
	serializer_class = SessionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		try:
			queryset = Session.objects.all().filter(habit__owner=self.request.user)
		except TypeError:
			raise NotAuthenticated
		else:
			return queryset

	@method_decorator(ensure_csrf_cookie)
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class ObtainAuthToken(DRFObtainAuthToken):

	@method_decorator(ensure_csrf_cookie)
	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data, context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		return Response({'token': token.key})


class UserRegistration(generics.CreateAPIView):
	serializer_class = UserSerializer
	permission_classes = (permissions.AllowAny,)

	def perform_create(self, serializer):
		data = serializer.validated_data
		email = data['email']
		if User.objects.filter(email=email).exists():
			raise serializers.ValidationError('A user with that email already exists.')
		serializer.save()

	def create(self, request, *args, **kwargs): # <- here i forgot self
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		token, created = Token.objects.get_or_create(user=serializer.instance)
		return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)

	@method_decorator(ensure_csrf_cookie)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)