from django.db import models

from core.models import TimeStampedModel


class Filiere(TimeStampedModel):
	code = models.CharField(max_length=20, unique=True, db_index=True)
	name = models.CharField(max_length=120, unique=True, db_index=True)
	description = models.TextField(blank=True)
	is_active = models.BooleanField(default=True, db_index=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return f'{self.code} - {self.name}'
