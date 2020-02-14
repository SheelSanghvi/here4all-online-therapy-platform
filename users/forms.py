from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm
from django.contrib.auth import get_user_model

class RegistrationForm(ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	confirm_password = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=[ 'email', 'user_type','f_name', 'l_name', 'gender','age', 'password', 'confirm_password']
		
		labels = {
        "f_name": "first name",
        "l_name": "last name",
    	}
	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")
		if password != confirm_password:
			raise forms.ValidationError("Passwords don't match")



class GuestContactUsForm(ModelForm):
	class Meta:
		model=GuestContactUs
		fields=['full_name', 'email', 'question'] 
		labels = {
        "email": "Email",
        "question": "What can we help you with?",
    	}

class BlogsForm(ModelForm):
	class Meta:
		model=Blogs
		fields=['topic', 'title', 'subtitle', 'image','content']
		labels={
		"content": "Write here!",
		"image": "Upload an image (optional)"
		}


class UserUpdate(ModelForm):
	class Meta:
		model=User
		fields=[ 'email', 'f_name', 'l_name','age', 'phone', 'image', 'additional_data']
		if get_user_model().user_type==2:
			labels = {
			"f_name": "first name",
			"l_name": "last name",
			"additional_data": "degree/speciality",
			}
		else:
			labels = {
			"f_name": "first name",
			"l_name": "last name",
			"additional_data": "health issues",
			}

# class ChatFormPatient(ModelForm):
# 	class Meta:
# 		model = Chat
# 		fields=['therapist', 'text']
# 		labels={
# 		"therapist": "Choose your therapist",
# 		"text": "Describe your issue",
# 		}



















