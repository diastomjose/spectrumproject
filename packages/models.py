
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



# Create your models here.

class Packages(models.Model):
	package_name = models.CharField(max_length = 100)
	package_no = models.IntegerField()
	package_cost = models.IntegerField()


class PlaceList(models.Model):
	place_name = models.CharField(max_length = 100)
	place_no = models.IntegerField()
	package_name = models.CharField(max_length = 100)
	# place_duration = models.IntegerField()
	place_description = models.CharField(max_length=1500)

	place_pic=models.FileField(upload_to='media/product_pics')

	class Meta:
		verbose_name = 'place_name'
		verbose_name_plural = 'place_name'
	def __unicode__ (self):
		return self.place_name

class OptionalPlaceList(models.Model):
	package_name = models.CharField(max_length=100)
	place_name = models.CharField(max_length = 100)
	place_no = models.IntegerField()
	place_cost = models.IntegerField()
	place_description = models.CharField(max_length=1500)


	# place_description = models.CharField(max_length = 500)

	place_pic=models.FileField(upload_to='media/product_pics')

	

	class Meta:
		verbose_name = 'optional_place_name'
		verbose_name_plural = 'optional_place_name'
	def __unicode__ (self):
		return self.place_name

class UserPackageList(models.Model):
	username = models.CharField(max_length=30)
	package_name = models.CharField(max_length=100)
	totalcost = models.IntegerField()
	allplaces = models.CharField(max_length=100)
	

	class Meta:
		verbose_name = 'username'
		verbose_name_plural = 'username' 
	def __unicode__(self):
		return self.username 


		
# class ReviewList(models.Model):
# 	username = models.CharField(max_length = 100)
