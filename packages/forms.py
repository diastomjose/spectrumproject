from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from packages.models import PlaceList




class AddPlacesForm(forms.ModelForm):
	class Meta:
		model = PlaceList
		fields = ['package_name','place_name','place_no','place_pic']


