from django.db import models


# Create your models here.
from django.dispatch import receiver


class Flag(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    enabled = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
