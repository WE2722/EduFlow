from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .services import DashboardAnalyticsService


@login_required
def dashboard_home(request):
	context = DashboardAnalyticsService.summary()

	if request.user.is_superuser or getattr(request.user, 'role', None) == 'admin':
		template_name = 'dashboard/home_admin.html'
	elif getattr(request.user, 'role', None) == 'staff':
		template_name = 'dashboard/home_staff.html'
	else:
		template_name = 'dashboard/home_viewer.html'

	return render(request, template_name, context)
