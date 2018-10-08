# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.views.generic import FormView,View,TemplateView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from customer.forms import UserForm,CustomerForm
from customer .models import ImageModel



import urllib
import urllib2
import json
# Create your views here.
class index(View):
	"""docstring for index"""
	template_name = 'index.html'
	model = ImageModel
	def get(self,request):
		obj1 = ImageModel.objects.all()
		context ={
		'obj1' : obj1
		}
		return render(request,self.template_name,context)
	


class RegisterCustomer(FormView):
	template_name ='register.html'
	form_class = UserForm 

	def get(self,request,*args,**kwargs):
		self.object = None
		form_class = self.get_form_class()
		user_form = self.get_form(form_class)
		cust_form = CustomerForm()
		return self.render_to_response(self.get_context_data(form1=user_form,form2=cust_form))
	def post(self,request,*args,**kwargs):
		self.object=None
		form_class = self.get_form_class()
		user_form = self.get_form(form_class)
		cust_form = CustomerForm(self.request.POST,self.request.FILES)
		if(user_form.is_valid() and cust_form.is_valid()):
			return self.form_valid(user_form,cust_form)
		else:
			return self.form_invalid(user_form,cust_form)
	def get_succes_url(self,**kwargs):
		return ('success')	


	def form_valid(self, user_form, cust_form):
		self.object = user_form.save()
		self.object.is_staff=True
		self.object.save()
		cust_obj = cust_form.save(commit=False)
		cust_obj.user_data = self.object
		cust_obj.save()
		return redirect('/login/')

	def form_invalid(self, user_form, cust_form):
	    return self.render_to_response(self.get_context_data(form1=user_form, form2=cust_form))










class LoginView(View):
	def get(self,request):
		template_name = 'login.html'
		context = {'form':AuthenticationForm(),'error':None}
		if request.user.is_authenticated():
			return redirect('home')
		return render(request,template_name,context)

	def post(self,request):
		f1 = request.POST.get('username')
		f2 = request.POST.get('password')
		user = authenticate(username=f1,password=f2)
		if user:
			if user.is_active:
				recaptcha_response = request.POST.get('g-recaptcha-response')
				url = 'https://www.google.com/recaptcha/api/siteverify'
				values = {
				'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
				'response': recaptcha_response
				}
				data = urllib.urlencode(values)
				req = urllib2.Request(url, data)
				response = urllib2.urlopen(req)
				result = json.load(response)
				if result['success']:
					login(request,user)
				else:
					print("//"*20,"Invalid reCaptcha")
				return redirect('home')
		template_name = 'login.html'
		context = {'form':AuthenticationForm(),'error':'Email or password incorrect!!'}
		return render(request,template_name,context)