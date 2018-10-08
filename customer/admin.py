# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from customer.models import Customer,ImageModel

from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Customer)
admin.site.register(ImageModel)