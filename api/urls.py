from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import FiliereViewSet, StudentViewSet, dashboard_stats

router = DefaultRouter()
router.register('students', StudentViewSet, basename='api-students')
router.register('filieres', FiliereViewSet, basename='api-filieres')

urlpatterns = [
    path('dashboard/', dashboard_stats, name='api-dashboard'),
] + router.urls
