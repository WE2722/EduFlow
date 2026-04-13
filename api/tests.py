from django.test import TestCase
from rest_framework.test import APIClient

from accounts.models import User
from filieres.models import Filiere
from students.models import Student


class APITests(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.user = User.objects.create_user(
			username='admin', password='pass12345', role=User.Role.ADMIN
		)
		self.client.force_authenticate(user=self.user)
		self.filiere = Filiere.objects.create(code='GI', name='Genie Industriel')
		self.student = Student.objects.create(
			first_name='Hana',
			last_name='Rami',
			email='hana@example.com',
			filiere=self.filiere,
			status='actif',
			created_by=self.user,
			updated_by=self.user,
		)

	def test_students_list_api(self):
		response = self.client.get('/api/v1/students/')
		self.assertEqual(response.status_code, 200)
		self.assertGreaterEqual(response.data['count'], 1)

	def test_dashboard_api(self):
		response = self.client.get('/api/v1/dashboard/')
		self.assertEqual(response.status_code, 200)
		self.assertIn('total_students', response.data)
