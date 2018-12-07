from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Habit, Session



class SessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Session
		fields = ('id', 'url', 'habit', 'name', 'text', 'date', 'is_complete')
		read_only_fields = ('name',)


class HabitSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	sessions = SessionSerializer(many=True, read_only=True)

	class Meta:
		model = Habit
		fields = ('id', 'url', 'owner',  'name', 'goal', 'start_date', 'stop_date', 'sessions')


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User(
			email=validated_data['email'],
			username=validated_data['username'],
		)
		user.set_password(validated_data['password'])
		user.save()
		return user