from django.core.management.base import BaseCommand

from my_app.models import Flag
from django.conf import settings

class Command(BaseCommand):
    help = "This will insert the initial data to the app"

    def handle(self, *args, **options):
        """
        Create the super user
        :param args:
        :param options:
        :return:
        """
        flag_name = settings.APPLICATION_FEATURE_FLAG
        if not Flag.objects.filter(name=flag_name).exists():
            Flag.objects.create(name=flag_name, enabled=True)
            print("initial data created")
        else:
            print("initial data already exists")
