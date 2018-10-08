# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from booking.models  import PackagePrice,BookedUser
# Register your models here.

admin.site.register(PackagePrice)

admin.site.register(BookedUser)
