# Create your views here.
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from structlog import get_logger

from django.conf import settings
from my_app.models import Flag


class Home(APIView):
    flag_name = settings.APPLICATION_FEATURE_FLAG
    logger = get_logger(__file__)

    def fetch_feature_flag(self):
        """
        This could involve a lot more than just fetching from db.
        In any case we have reduced greatly the hits on the database

        :return:
        """
        # pull the feature flag value from the db and log the pull
        flag = Flag.objects.get(name=self.flag_name)
        return flag.enabled

    def get(self, request):
        # attempt to get the feature from cache
        flag_enabled = cache.get(self.flag_name)

        # if not set, fetch from db and update the cache
        if flag_enabled not in [True, False]:
            flag_enabled = self.fetch_feature_flag()

            # update the cache for next time
            cache.set(self.flag_name, flag_enabled, settings.CACHE_TTL)
            self.logger.info("fetched from the db")
        else:
            self.logger.info("fetched from the cache")

        return Response(
            {
                "status": "success",
                self.flag_name: flag_enabled,
            }
        )
