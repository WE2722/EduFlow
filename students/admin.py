from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = (
		'last_name',
		'first_name',
		'email',
		'filiere',
		'status',
		'date_inscription',
		'created_by',
		'updated_by',
	)
	search_fields = ('last_name', 'first_name', 'email', 'filiere__name', 'filiere__code')
	list_filter = ('filiere', 'status')
	list_select_related = ('filiere', 'created_by', 'updated_by')
