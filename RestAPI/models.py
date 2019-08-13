# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Location(models.Model):
	lat = models.DecimalField(max_digits=6,decimal_places=3)
	lon = models.DecimalField(max_digits=6,decimal_places=3)
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=25)

class Weather(models.Model):
	id = models.IntegerField(primary_key=True)
	date = models.CharField(max_length=20)
	temperature = models.TextField()
	location = models.ForeignKey('Location',on_delete=models.CASCADE)