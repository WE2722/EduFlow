from django.test import TestCase
from django.db import IntegrityError

from .models import Filiere


class FiliereModelTests(TestCase):
	def test_unique_code(self):
		Filiere.objects.create(code='DS', name='Data Science')
		with self.assertRaises(IntegrityError):
			Filiere.objects.create(code='DS', name='Different Name')
