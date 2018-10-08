
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from datetime import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse


from django.views.generic import TemplateView,View


from booking.models import PackagePrice,BookedUser

from django.template.loader import render_to_string

import tempfile
from weasyprint import HTML
# from tourismproject.packages.models import  UserPackageList

# Create your views here.


class PackagePriceView(View):
	template_name = 'packageprice.html'
	model = PackagePrice
	def get(self,request):
		
		totalcost = request.session['totalcost']
		print('packageprice =', totalcost)
		
		time = datetime.now()
	
		context = {
		'time' : time,
		'totalcost' : totalcost,
		}

		return render(request,self.template_name,context)

	def post(self,request):
		print('hello')
		num1 = request.POST.get('tcost')
		print('helloummy',num1)
		num2 = request.POST.get('num')
		request.session['num'] = num2
		request.session['tcost'] = num1
		print(num2)
		return redirect('/booked/')

class BookedUserView(View):
	template_name = 'book.html'
	model = BookedUser

	def get(self,request):
		print('rum',request.session['tcost'])
		return render(request,self.template_name)

	def post(self,request):
		str1 = request.session['pcknme']
		str2 = request.user.username

		obj1 = BookedUser(booked_user = str(str2),booked_package = str(str1))

		obj1.save()

		return redirect('/customer/')


def generate_pdf(request):
    # obj1 = UserPackageList.filter(username = request.user.username)
    # str1 = obj1[0].allplaces
    nam = request.session['package_name']
    username =request.user.username
    tcost =request.session['tcost'] 
    print(tcost)

    no =  request.session['num'] 
    print(no)
    html_string = render_to_string('download.html',{'nam':nam,'username' : username , 'tcost' : tcost,'no' : no})
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'r')
        response.write(output.read())

    return response


class DownloadView(View):
  	template_name = 'download.html'

  	def get (self,request):
  		tcost = request.session['tcost']
  		print('hello')
  		no = request.session['num']
  		print(no)
  		nam = request.session['package_name']
  		context = {
  		'tcost' : tcost,
  		'no' : no,
  		'nam' : nam,
  		}
  		return render(request,self.template_name,context)
  		


