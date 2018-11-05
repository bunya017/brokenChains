from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Habit, Session



class SessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Session
		fields = ('url', 'habit', 'name', 'text', 'date', 'is_complete')


class HabitSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	sessions = SessionSerializer(many=True, read_only=True)

	class Meta:
		model = Habit
		fields = ('url', 'owner',  'name', 'goal', 'start_date', 'stop_date', 'sessions')



