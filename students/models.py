from django.db import models

from core.models import AuditModel
from filieres.models import Filiere


class Student(AuditModel):
	STATUS_CHOICES = [
		('actif', 'Actif'),
		('suspendu', 'Suspendu'),
		('diplome', 'Diplome'),
	]

	first_name = models.CharField('Prenom', max_length=100, db_index=True)
	last_name = models.CharField('Nom', max_length=100, db_index=True)
	email = models.EmailField('Email', unique=True, db_index=True)
	phone = models.CharField('Telephone', max_length=20, blank=True)
	filiere = models.ForeignKey(Filiere, on_delete=models.PROTECT, related_name='students')
	photo = models.ImageField(upload_to='students/photos/', blank=True, null=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='actif', db_index=True)
	date_inscription = models.DateTimeField(auto_now_add=True, db_index=True)

	class Meta:
		ordering = ['-date_inscription']
		indexes = [
			models.Index(fields=['last_name', 'first_name']),
			models.Index(fields=['status', 'date_inscription']),
		]

	def __str__(self):
		return f'{self.last_name} {self.first_name}'
