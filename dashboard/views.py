from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .services import DashboardAnalyticsService


@login_required
def dashboard_home(request):
	context = DashboardAnalyticsService.summary()
	return render(request, 'dashboard/home.html', context)
