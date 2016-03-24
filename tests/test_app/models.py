# -*- coding: utf-8 -*-
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
