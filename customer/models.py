# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
	user_data = models.OneToOneField(User)
	place = models.CharField(max_length = 50)
	address = models.CharField(max_length = 50)
	zipcode = models.IntegerField()


	def __str__(self):
		return self.place
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
	user_data = models.OneToOneField(User)
	place = models.CharField(max_length = 50)
	address = models.CharField(max_length = 50)
	zipcode = models.IntegerField()


	def __str__(self):
		return self.place







class ImageModel(models.Model):
	image_name = models.CharField(max_length=40)
	pic=models.FileField(upload_to='media/product_pics')

	class Meta:
		verbose_name = 'image_name'
		verbose_name_plural = 'image_name'
	def __unicode__ (self):
		return self.image_name