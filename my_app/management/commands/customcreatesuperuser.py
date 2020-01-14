from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This will create the initial super user"

    def handle(self, *args, **options):
        """
        Create the super user
        :param args:
        :param options:
        :return:
        """
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='emmanuelt2009@gmail.com',
                password='admin'
            )
            print("superuser created")
        else:
            print("superuser already exists")
