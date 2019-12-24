from django.db import models

from .data_item import DataItem


class DataContainer(models.Model):

    date_created  = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    name  = models.CharField(max_length=200)
    items = models.ManyToManyField(DataItem)