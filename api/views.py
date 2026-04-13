from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from filieres.models import Filiere
from students.models import Student

from .permissions import IsStaffOrReadOnly
from .serializers import FiliereSerializer, StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.select_related('filiere').all().order_by('-date_inscription')
	serializer_class = StudentSerializer
	permission_classes = [IsStaffOrReadOnly]
	filterset_fields = ['status', 'filiere']
	search_fields = ['first_name', 'last_name', 'email', 'phone']
	ordering_fields = ['date_inscription', 'last_name', 'status']

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user, updated_by=self.request.user)

	def perform_update(self, serializer):
		serializer.save(updated_by=self.request.user)


class FiliereViewSet(viewsets.ModelViewSet):
	queryset = Filiere.objects.all().order_by('name')
	serializer_class = FiliereSerializer
	permission_classes = [IsStaffOrReadOnly]
	filterset_fields = ['is_active']
	search_fields = ['code', 'name']
	ordering_fields = ['name', 'code', 'created_at']


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request, version=None):
	total_students = Student.objects.count()
	students_per_filiere = list(
		Student.objects.values('filiere__name').annotate(total=Count('id')).order_by('filiere__name')
	)
	status_distribution = list(
		Student.objects.values('status').annotate(total=Count('id')).order_by('status')
	)
	recent_students = list(
		Student.objects.select_related('filiere')
		.values('id', 'first_name', 'last_name', 'email', 'filiere__name', 'status', 'updated_at')
		.order_by('-updated_at')[:10]
	)

	return Response(
		{
			'total_students': total_students,
			'students_per_filiere': students_per_filiere,
			'status_distribution': status_distribution,
			'recent_activity': recent_students,
		}
	)
