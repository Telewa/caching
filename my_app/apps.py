from django.apps import AppConfig
from django.db.models.signals import post_save


class MyAppConfig(AppConfig):
    name = 'my_app'

    def ready(self):
        """
        call the flag_updated with new data on post_save of Flag

        :return:
        """
        from my_app.models import Flag  # noqa
        from my_app.signals import flag_updated  # noqa
        post_save.connect(flag_updated, sender=Flag)
