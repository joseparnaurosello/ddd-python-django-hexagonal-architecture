# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
