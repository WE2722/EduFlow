import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from filieres.models import Filiere
from students.models import Student


class Command(BaseCommand):
    help = 'Seed demo users, filieres, and students for EduFlow.'

    def handle(self, *args, **options):
        User = get_user_model()

        admin_user, _ = User.objects.get_or_create(
            username='admin', defaults={'email': 'admin@eduflow.local', 'role': 'admin', 'is_staff': True, 'is_superuser': True}
        )
        admin_user.set_password('admin12345')
        admin_user.role = 'admin'
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()

        staff_user, _ = User.objects.get_or_create(
            username='staff', defaults={'email': 'staff@eduflow.local', 'role': 'staff', 'is_staff': True}
        )
        staff_user.set_password('staff12345')
        staff_user.role = 'staff'
        staff_user.is_staff = True
        staff_user.save()

        viewer_user, _ = User.objects.get_or_create(
            username='viewer', defaults={'email': 'viewer@eduflow.local', 'role': 'viewer', 'is_staff': False}
        )
        viewer_user.set_password('viewer12345')
        viewer_user.role = 'viewer'
        viewer_user.is_staff = False
        viewer_user.save()

        filieres_payload = [
            ('IA', 'Intelligence Artificielle'),
            ('DS', 'Data Science'),
            ('GI', 'Genie Industriel'),
            ('SE', 'Systemes Embarques'),
        ]

        filieres = []
        for code, name in filieres_payload:
            filiere, _ = Filiere.objects.get_or_create(code=code, defaults={'name': name, 'is_active': True})
            if filiere.name != name:
                filiere.name = name
                filiere.save(update_fields=['name'])
            filieres.append(filiere)

        first_names = ['Sara', 'Ali', 'Youssef', 'Hana', 'Mariam', 'Omar', 'Ines', 'Nora', 'Mehdi', 'Salma']
        last_names = ['Bennani', 'Karimi', 'Rami', 'El Idrissi', 'Alaoui', 'Fassi', 'Mouline', 'Kabbaj']
        statuses = ['actif', 'suspendu', 'diplome']

        created_count = 0
        for idx in range(1, 26):
            first = random.choice(first_names)
            last = random.choice(last_names)
            email = f'{first.lower()}.{last.lower()}{idx}@example.com'
            _, created = Student.objects.get_or_create(
                email=email,
                defaults={
                    'first_name': first,
                    'last_name': last,
                    'phone': f'06{random.randint(10000000, 99999999)}',
                    'filiere': random.choice(filieres),
                    'status': random.choice(statuses),
                    'created_by': admin_user,
                    'updated_by': admin_user,
                },
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS('Demo seed completed successfully.'))
        self.stdout.write(f'Users: admin/staff/viewer created or updated.')
        self.stdout.write(f'Filieres available: {Filiere.objects.count()}')
        self.stdout.write(f'New students created: {created_count}')
