from django.db.models import Count

from students.models import Student


class DashboardAnalyticsService:
    @staticmethod
    def summary():
        students = Student.objects.select_related('filiere')
        total_students = students.count()
        status_distribution = list(
            students.values('status').annotate(total=Count('id')).order_by('status')
        )
        students_per_filiere = list(
            students.values('filiere__name').annotate(total=Count('id')).order_by('filiere__name')
        )
        recent_activity = students.order_by('-updated_at')[:8]

        return {
            'total_students': total_students,
            'status_distribution': status_distribution,
            'students_per_filiere': students_per_filiere,
            'recent_activity': recent_activity,
        }
