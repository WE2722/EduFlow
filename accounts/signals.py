from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name != 'accounts':
        return

    for group_name in ('Admin', 'Staff', 'Viewer'):
        Group.objects.get_or_create(name=group_name)
