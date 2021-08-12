# -*- coding: utf-8 -*-

from django.db import models
import datetime 
from user.models  import User

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))


class User_Email(models.Model):
    email_name=models.CharField(max_length=50)

    email_user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)    

 
class Language(models.Model):
    name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)    


# class Email(models.Model):
#     email_name=models.CharField(max_length=50)

#     email_user=models.ForeignKey(User,on_delete=models.CASCADE)
#     created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
#     modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)    


class Personal_Details(models.Model):

    first_name=models.CharField(max_length=10)
    middle_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)  
    dob=models.DateTimeField() 
    # email=models.ForeignKey(Email,on_delete=models.CASCADE)
    contact=models.IntegerField(max_length=10)

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)


   
class Other_link(models.Model):   
    link=models.URLField(max_length = 200,blank=True)
    name=models.CharField(max_length=10,default="")
    # EmailField(verbose_name='email', max_length=20, unique=True)

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)    
                  

class Objectives(models.Model):
    objective_text=models.TextField(default="Enter Obejective")

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)

class Education(models.Model):
    board=models.CharField(max_length=50)
    degree=models.CharField(max_length=50)
    date_from=models.DateField(null=True)
    date_to=models.DateField(null=True)
    about=models.TextField(default="Enter Details")
    marks=models.TextField(default="here education")

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)

# class urresume(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     education=models.TextField(default="here education")
#     date_from=models.DateTimeField(null=True)
#     date_to=models.DateTimeField(null=True)
#     marks=models.TextField(default="here education")

#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
#     modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)

class Experience(models.Model):
    company=models.CharField(max_length=20)
    # date=models.DateTimeField(null=True)
    date_from=models.DateField(null=True)
    date_to=models.DateField(null=True)
    total_experience_time=models.IntegerField(max_length=10)
    summary=models.TextField(default="Enter Summary")

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)
# import datetime

class Projects(models.Model):
    title=models.CharField(max_length=50)
    date_from=models.DateField(null=True)
    date_to=models.DateField(null=True)
    technogy_used=models.CharField(max_length=100)
    total_member=models.IntegerField(max_length=20)
    your_role=models.CharField(max_length=20)
    summary=models.TextField(default="Enter Summary")

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)

class Skills(models.Model):
    name=models.CharField(max_length=20)

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)              

class Certification(models.Model):
    name=models.CharField(max_length=20)
    date_from=models.DateField(null=True)
    date_to=models.DateField(null=True)
    expired_date=models.TextField(default="Enter Expired Date",blank=None) 
    about=models.TextField(default="Enter Details")

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)

class Address(models.Model):
    flat_no=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pincode=models.IntegerField(max_length=20)
    country=models.CharField(max_length=20)

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)

class Interest(models.Model):
    name=models.CharField(max_length=20)

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    modified_at=models.DateTimeField(verbose_name='Modified At', auto_now=True)    
    
# CATEGORY_CHOICES2 = (
#     ('0', 0),
#     ('1', 1),
#     ('2', 2),
    
# )
