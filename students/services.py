from django.db.models import Q

from .models import Student


class StudentQueryService:
    @staticmethod
    def filtered_students(query='', filiere='', status=''):
        students = Student.objects.select_related('filiere', 'created_by', 'updated_by')

        if query:
            students = students.filter(
                Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
                | Q(email__icontains=query)
                | Q(phone__icontains=query)
            )

        if filiere:
            students = students.filter(filiere__id=filiere)

        if status:
            students = students.filter(status=status)

        return students


class StudentCommandService:
    @staticmethod
    def create_student(form, actor):
        student = form.save(commit=False)
        student.created_by = actor
        student.updated_by = actor
        student.save()
        return student

    @staticmethod
    def update_student(form, actor):
        student = form.save(commit=False)
        student.updated_by = actor
        student.save()
        return student
