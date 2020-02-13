from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import CustomUser

class CustomUserCreateTestCase(APITestCase):
  def test_create_user(self):
    initial_user_count = CustomUser.objects.count()
    user_attrs = {
      'username': 'Michael',
      'points': 0,
      'level': 1,
      'email': 'michael@email.com',
      'password': '1nsecure_passw0rd'
    }
    response = self.client.post('/user/', user_attrs)
    self.assertEqual(response.status_code, 201)
  def test_update_user(self):
    initial_user_count = CustomUser.objects.count()
    user_attrs = {
      'username': 'Michael',
      'points': 0,
      'level': 1,
      'email': 'michael@email.com',
      'password': '1nsecure_passw0rd'
    }
    response = self.client.post('/user/', user_attrs)
    user_attrs_updated = {
      'username': 'Michael',
      'points': 50,
      'level': 5,
      'email': 'michael@email.com',
      'password': 'B3TT3r_p@55w0rd'
    }
    response = self.client.put('/user/1/', user_attrs_updated)
    self.assertEqual(response.status_code, 200)
