# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from packages.models import Packages,PlaceList,OptionalPlaceList,UserPackageList

# Register your models here.

admin.site.register(Packages)
admin.site.register(PlaceList)
admin.site.register(OptionalPlaceList)
admin.site.register(UserPackageList)

