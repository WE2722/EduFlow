from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from filieres.models import Filiere

from .models import Student


class StudentViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='staff', password='pass12345', role=User.Role.STAFF
        )
        self.client.force_login(self.user)
        self.filiere = Filiere.objects.create(code='IA', name='Intelligence Artificielle')
        self.student = Student.objects.create(
            first_name='Ali',
            last_name='Karimi',
            email='ali@example.com',
            phone='0600000000',
            filiere=self.filiere,
            status='actif',
            created_by=self.user,
            updated_by=self.user,
        )

    def test_create_student(self):
        response = self.client.post(
            reverse('student_create'),
            {
                'first_name': 'Sara',
                'last_name': 'Bennani',
                'email': 'sara@example.com',
                'phone': '0611111111',
                'filiere': self.filiere.id,
                'status': 'suspendu',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Student.objects.filter(email='sara@example.com').exists())

    def test_list_search_and_filter(self):
        response = self.client.get(
            reverse('student_list'), {'q': 'ali', 'status': 'actif', 'filiere': self.filiere.id}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ali@example.com')

    def test_update_student(self):
        response = self.client.post(
            reverse('student_update', args=[self.student.pk]),
            {
                'first_name': 'Ali',
                'last_name': 'Karimi',
                'email': 'ali.updated@example.com',
                'phone': '0600000000',
                'filiere': self.filiere.id,
                'status': 'actif',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.student.refresh_from_db()
        self.assertEqual(self.student.email, 'ali.updated@example.com')

    def test_delete_student(self):
        response = self.client.post(reverse('student_delete', args=[self.student.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())

    def test_csv_export(self):
        response = self.client.get(reverse('export_students_csv'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')
        self.assertIn('ali@example.com', response.content.decode('utf-8'))

    def test_ajax_search(self):
        response = self.client.get(reverse('student_ajax_search'), {'q': 'ali'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.json())
