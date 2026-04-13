import csv

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from core.permissions import role_required
from filieres.models import Filiere

from .forms import StudentForm
from .models import Student
from .services import StudentCommandService, StudentQueryService


@login_required
def student_list(request):
	query = request.GET.get('q', '').strip()
	filiere = request.GET.get('filiere', '').strip()
	status = request.GET.get('status', '').strip()

	students = StudentQueryService.filtered_students(query=query, filiere=filiere, status=status)

	paginator = Paginator(students, 5)
	page_obj = paginator.get_page(request.GET.get('page'))

	return render(
		request,
		'students/student_list.html',
		{
			'page_obj': page_obj,
			'query': query,
			'filiere': filiere,
			'status': status,
			'status_choices': Student.STATUS_CHOICES,
			'filieres': Filiere.objects.filter(is_active=True).order_by('name'),
			'total_students': students.count(),
		},
	)


@login_required
@role_required('admin', 'staff')
def student_create(request):
	form = StudentForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		StudentCommandService.create_student(form, request.user)
		messages.success(request, 'Etudiant ajoute avec succes.')
		return redirect('student_list')
	return render(request, 'students/student_form.html', {'form': form, 'title': 'Ajouter'})


@login_required
def student_detail(request, pk):
	student = get_object_or_404(Student, pk=pk)
	return render(request, 'students/student_detail.html', {'student': student})


@login_required
@role_required('admin', 'staff')
def student_update(request, pk):
	student = get_object_or_404(Student, pk=pk)
	form = StudentForm(request.POST or None, request.FILES or None, instance=student)
	if form.is_valid():
		StudentCommandService.update_student(form, request.user)
		messages.success(request, 'Etudiant modifie avec succes.')
		return redirect('student_list')
	return render(
		request,
		'students/student_form.html',
		{'form': form, 'student': student, 'title': 'Modifier'},
	)


@login_required
@role_required('admin', 'staff')
def student_delete(request, pk):
	student = get_object_or_404(Student, pk=pk)
	if request.method == 'POST':
		student.delete()
		messages.warning(request, 'Etudiant supprime.')
		return redirect('student_list')
	return render(request, 'students/student_confirm_delete.html', {'student': student})


@login_required
@role_required('admin', 'staff')
def export_students_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="etudiants.csv"'

	writer = csv.writer(response)
	writer.writerow(['Prenom', 'Nom', 'Email', 'Telephone', 'Filiere', 'Statut'])

	for student in Student.objects.select_related('filiere').all().order_by('-date_inscription'):
		writer.writerow(
			[
				student.first_name,
				student.last_name,
				student.email,
				student.phone,
				student.filiere.name,
				student.get_status_display(),
			]
		)

	return response


@login_required
def student_ajax_search(request):
	query = request.GET.get('q', '').strip()
	students = StudentQueryService.filtered_students(query=query)[:10]
	data = [
		{
			'id': student.pk,
			'full_name': f'{student.last_name} {student.first_name}',
			'email': student.email,
			'filiere': student.filiere.name,
			'status': student.get_status_display(),
		}
		for student in students
	]
	return JsonResponse({'results': data})
