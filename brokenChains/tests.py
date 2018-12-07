from django.contrib.auth .models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .models import Habit, Session



class UserRegistrationTest(APITestCase):
	def test_user_registration(self):
		"""
		Test user can register.
		"""
		data = {
			'username': 'testUser',
			'email': 'testEmail@mail.com',
			'password': 'testPassword'
		}
		url = reverse('user-registration')
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserAuthenticationTests(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user('testUser', 'testEmail@email.com', 'testPassword')
		self.data = {
			'username': 'testUser',
			'password': 'testPassword'
		}

	def test_get_user_auth_token(self):
		"""
		Test user can get authentication token.
		"""
		url = reverse('get-auth-token')
		response = self.client.post(url, self.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateHabitTest(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user('testUser', 'testEmail@email.com', 'testPassword')
		self.client.login(username='testUser', password='testPassword')
		self.url = reverse('habits-list')
		self.data = {
			'name': 'study',
			'goal': 'to be literate.',
			'stop_date': '2018-12-30'
		}

	def test_can_create_habit(self):
		"""
		Test user can create new habit.
		"""
		response = self.client.post(self.url, self.data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadHabitTest(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user('testUser', 'testEmail@email.com', 'testPassword')
		self.client.login(username='testUser', password='testPassword')
		self.new_habit = Habit(
			owner=self.user,
			name='Work out',
			goal='physical fitness.',
			stop_date='2018-12-30'
		)
		self.new_habit.save()

	def test_can_read_habits_list(self):
		"""
		Test user can read habits list.
		"""
		response = self.client.get(reverse('habits-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_can_read_habit_detail(self):
		"""
		Test user can read habit detail.
		"""
		response = self.client.get(reverse('habit-detail', args=[self.new_habit.id]))
		self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateSessionTest(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user('testUser', 'testEmail@email.com', 'testPassword')
		self.client.login(username='testUser', password='testPassword')
		self.url = reverse('sessions-list')
		self.habit = Habit(
			owner=self.user,
			name='Work out',
			goal='physical fitness.',
			stop_date='2018-12-30'
		)
		self.habit.save()
		self.data = {
			'habit': self.habit.id,
			'text': 'finally started',
		}

	def test_can_create_session(self):
		"""
		Test user can create new session.
		"""
		response = self.client.post(self.url, self.data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadSessionTest(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user('testUser', 'testEmail@email.com', 'testPassword')
		self.client.login(username='testUser', password='testPassword')
		self.habit = Habit(
			owner=self.user,
			name='Work out',
			goal='physical fitness.',
			stop_date='2018-12-30'
		)
		self.habit.save()
		self.session = Session(
			habit=self.habit,
			text='finally started'
		)
		self.session.save()

	def test_can_read_sessions_list(self):
		"""
		Test user can read sessions list.
		"""
		response = self.client.get(reverse('sessions-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_can_read_session_detail(self):
		"""
		Test user can read session detail.
		"""
		response = self.client.get(reverse('session-detail', args=[self.session.id]))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
