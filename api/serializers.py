from rest_framework import serializers

from filieres.models import Filiere
from students.models import Student


class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = ['id', 'code', 'name', 'description', 'is_active', 'created_at', 'updated_at']


class StudentSerializer(serializers.ModelSerializer):
    filiere_name = serializers.CharField(source='filiere.name', read_only=True)

    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'filiere',
            'filiere_name',
            'photo',
            'status',
            'date_inscription',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['date_inscription', 'created_at', 'updated_at']
