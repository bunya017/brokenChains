from django.contrib.auth .models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Habit, Session



class UserRegistrationTest(APITestCase):
	def test_user_registration(self):
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
		url = reverse('get-auth-token')
		response = self.client.post(url, self.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
