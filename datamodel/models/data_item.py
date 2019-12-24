from django.contrib.postgres.fields import JSONField
from django.db import models

from .data_container import DataContainer


class DataItem(models.Model):

    date_created  = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    data       = JSONField()
    containers = models.ManyToManyField(DataContainer)
    name       = models.CharField(max_length=200)

    def __str__(self):
        return self.name