# -*- coding: utf-8 -*-

from django import forms

from .models import User_Email,  Language,Personal_Details,Other_link , Language,Objectives , Education , Experience , Projects, Skills , Certification,Address ,Interest

from user.models import User
from django.forms import ModelForm
from django import forms


class testform(forms.Form):

	text_fields = forms.CharField(label='text_fields')
	

class Registrationform(ModelForm):

	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
	
	class Meta:
		model=User
		fields=['first_name','last_name','email']
		
	
			
		
	def clean_password2(self):
		pwd1 = self.cleaned_data.get('password1')
		pwd2 = self.cleaned_data.get('password2')
		if not pwd1 or not pwd2:
			raise forms.ValidationError('Password is empty')
		if pwd1 != pwd2:
			raise forms.ValidationError('Passwords do not match')
		return pwd2


	def save(self, commit=True):
		user = super(Registrationform,self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
		    user.save()
		return user			

class Email_form(ModelForm):
	class Meta:
		model=User_Email
		fields=['email_name','email_user']



class Skills_form(ModelForm):
	class Meta:
		model=Skills
		fields=['name','user']

class Language_form(ModelForm):
	class Meta:
		model=Interest
		fields=['name','user']



class Address_form(ModelForm):
	class Meta:
		model=Address
		fields=['flat_no','city','state','pincode','country','user']

class Certification_form(ModelForm):
	class Meta:
		model=Certification
		fields=['name','date_from','date_to','expired_date','about','user']
		widgets = {'date_from':forms.widgets.DateTimeInput(format="%Y-%m-%d %H:%M:%S",attrs={'placeholder':"YY-MM-DD HH:MM:SS",'type':"datetime"}),
		'date_to':forms.widgets.DateTimeInput(format="%Y-%m-%d %H:%M:%S",attrs={'placeholder':"YY-MM-DD HH:MM:SS",'type':"datetime"}),
		'expired_date':forms.widgets.DateTimeInput(format="%Y-%m-%d %H:%M:%S",attrs={'placeholder':"YY-MM-DD HH:MM:SS",'type':"datetime"}),}
		# widgets = {'date_to':forms.widgets.DateTimeInput(format="%d/%m/%Y %H:%M:%S",attrs={'placeholder':"DD/MM/DD HH:MM:SS",'type':"date"}),}


class Projects_form(ModelForm):
	class Meta:
		model=Projects
		fields=['title','date_from','date_to','technogy_used', 'total_member','your_role','summary','user']
		widgets = {'date_from':forms.widgets.DateTimeInput(format="%Y-%m-%d %H:%M:%S",attrs={'placeholder':"YY-MM-DD HH:MM:SS",'type':"datetime"}),
		'date_to':forms.widgets.DateTimeInput(format="%Y-%m-%d %H:%M:%S",attrs={'placeholder':"YY-MM-DD HH:MM:SS",'type':"datetime"}),}


class Experience_form(ModelForm):
	class Meta:
		model=Experience
		fields=['company','date_from','date_to','total_experience_time','summary','user']
		widgets = {'date_from':forms.widgets.DateTimeInput(format="%Y-%m-%d %H:%M:%S",attrs={'placeholder':"YY-MM-DD HH:MM:SS",'type':"datetime"}),
		'date_to':forms.widgets.DateTimeInput(format="%Y-%m-%d %H:%M:%S",attrs={'placeholder':"YY-MM-DD HH:MM:SS",'type':"datetime"}),}

class Education_form(ModelForm):
	class Meta:
		model=Education
		fields=['id','board','degree','marks','date_from','date_to','about','user']
		widgets = {'date_from':forms.widgets.DateTimeInput(format="%Y-%m-%d %H:%M:%S",attrs={'placeholder':"YY-MM-DD HH:MM:SS",'type':"datetime"}),
		'date_to':forms.widgets.DateTimeInput(format="%Y-%m-%d %H:%M:%S",attrs={'placeholder':"YY-MM-DD HH:MM:SS",'type':"datetime"}),}



class Objectives_form(ModelForm):
	class Meta:
		model=Objectives
		fields=['objective_text','user']


class Personal_Details_form(ModelForm):
	class Meta:
		model=Personal_Details
		fields=['first_name','middle_name','last_name','dob','contact','user']
		widgets = {'dob':forms.widgets.DateTimeInput(format="%Y-%m-%d %H:%M:%S",attrs={'placeholder':"DD/MM/DD HH:MM:SS",'type':"datetime"}),}




class Other_link_form(ModelForm):
	class Meta:
		model=Other_link
		fields=['link','name','user']

class Interest_form(ModelForm):
	class Meta:
		model=Interest
		fields=['name','user']		

class Language_form(ModelForm):
	class Meta:
		model=Language
		fields=['name','user']


# class User_table(ModelForm):
# 	class Meta:
# 		fields=["first_name",
#     "last_name",
#     "user_email",
#     "date_joined",
#     "last_login",
#     "is_admin",
#     "is_active",
#     "is_staff",
#  ]