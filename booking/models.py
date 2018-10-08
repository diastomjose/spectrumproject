# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class PackagePrice(models.Model):
	package_price = models.IntegerField()
	package_name = models.CharField(max_length = 100)

	class Meta:
		verbose_name = 'package_price'
		verbose_name_plural = 'package_price'
	def __str__(self):
		return self.package_name

class BookedUser(models.Model):
	booked_user = models.CharField(max_length = 100)
	booked_package = models.CharField(max_length = 100)

	class Meta:
		verbose_name = 'booked_user'
		verbose_name_plural = 'booked_user'

	def __str__(self):
		return self.booked_user




