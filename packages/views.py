# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.views.generic import TemplateView,View,CreateView
from django.db import connection


from packages.models import Packages,PlaceList,OptionalPlaceList,UserPackageList
from packages.forms import AddPlacesForm
# Create your views here.

class PackagesView(View):
	template_name = 'package.html'
	model = Packages

	def get(self,request):
		obj1 = Packages.objects.all()
		context = {
		'obj1' : obj1,
		}

		return render(request,self.template_name,context)
	def post (self,request):
		str1 = request.POST.get('selectedPackage')
		
		request.session['package_name'] = str1
		# print(str1)
		# num1 = Packages.objects.filter(package_name = str1) .only('package_no')
		# print( connection.queries[-1])
		return redirect('/places/')


class PlaceListView(View):
	template_name = 'placelist.html'
	model = PlaceList

	def get(self,request):
		str1 = request.session['package_name']
		
		obj1 = PlaceList.objects.filter(package_name = str(str1))

		obj2 = OptionalPlaceList.objects.filter(package_name = str(str1))
		context = {
		'obj1' : obj1,
		'obj2'  : obj2,
		}
		return render(request,self.template_name,context)
	def post(self,request):
		str1 = request.POST.get('packagename')
		print('hello',str1)

		some_var = request.POST.getlist('checks[]')

		# print(obj3,"==================")
		# print(obj3[0].place_cost)
		sumcost = 0
		placeList = ''
		for i in some_var:
			obj3 = OptionalPlaceList.objects.filter(place_name=str(i))
			sumcost += obj3[0].place_cost
			placeList = placeList + i + ','

		print(sumcost)

		obj4 = Packages.objects.filter(package_name = request.session['package_name'])
		package_cost = obj4[0].package_cost
		totalcost = sumcost + package_cost
		print(totalcost)


		obj5 = PlaceList.objects.filter(package_name=request.session['package_name'])
		for i in obj5:
			placeList = placeList + i.place_name + ','
		print(placeList)	

		obj6 = UserPackageList(username = request.user.username, package_name = request.session['package_name'], totalcost = totalcost, allplaces = placeList)

		obj6.save()
		request.session['totalcost'] = totalcost	


			

		request.session['pcknme'] = str(str1)
		return redirect('/packageprice/')

class AddPackagesView(View):
	template_name = 'addpackage.html'
	model = Packages

	def get(self,request):
		return render(request,self.template_name)


	def post(self,request):
		str1 = request.POST.get('addpackages_packagename')
		print(str1)
		num1 = request.POST.get('addpackages_packageno')
		print(num1)
		obj1 = Packages(package_name = str(str1),package_no = int(num1))
		obj1.save()
		return redirect('/addpackages/')


class AddPlacesView(CreateView):
	template_name = 'addplace.html'
	form_class = AddPlacesForm

	
