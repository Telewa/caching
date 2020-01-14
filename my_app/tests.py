from unittest import mock

from django.conf import settings
from django.core.cache import cache
from django.test import TestCase
from rest_framework.reverse import reverse

from my_app.models import Flag


class TestFlags(TestCase):
    flag_name = settings.APPLICATION_FEATURE_FLAG

    def setUp(self):
        Flag.objects.create(name=self.flag_name, enabled=True)
        self.assertTrue(Flag.objects.all().exists())
        cache.clear()

    def tearDown(self):
        cache.clear()

    def test_flags_created(self):
        response = self.client.get(reverse("home"))
        self.assertEquals(
            response.json(),
            {
                'status': 'success',
                settings.APPLICATION_FEATURE_FLAG: True
            }
        )

    @mock.patch("my_app.views.Home.fetch_feature_flag", autospec=True)
    def test_updating_flags(self, fetch_feature_flag):
        fetch_feature_flag.return_value = False

        for i in range(10):
            response = self.client.get(reverse("home"))

            self.assertEquals(
                response.json(),
                {
                    'status': 'success',
                    settings.APPLICATION_FEATURE_FLAG: False
                }
            )

        # the call to the database should only happen once, once the item has been cached
        self.assertEqual(fetch_feature_flag.call_count, 1)

        # this should send a signal to invalidate the cache
        flag = Flag.objects.get(name=self.flag_name)
        flag.enabled = False
        flag.save()

        for i in range(10):
            response = self.client.get(reverse("home"))

            self.assertEquals(
                response.json(),
                {
                    'status': 'success',
                    settings.APPLICATION_FEATURE_FLAG: False
                }
            )

        # the call to the database should only happen once, once the item has been updated in cache
        self.assertEqual(fetch_feature_flag.call_count, 2)


