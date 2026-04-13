from django.contrib import admin

from .models import Filiere


@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
	list_display = ('code', 'name', 'is_active', 'created_at', 'updated_at')
	search_fields = ('code', 'name')
	list_filter = ('is_active',)
