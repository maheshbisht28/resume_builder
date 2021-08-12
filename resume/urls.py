# from django.contrib import admin
from django.urls import path, include
from  .views import *
from django.contrib.auth import views as auth_views
# print("fefe")
urlpatterns = [

path('register/',register, name="register"),
path('enter_details/',enter_details, name="enter_details"),
path('show_details/',show_details, name="show_details"),
path('resume_template/',resume_template, name="resume_template"),
path('make_resume/',make_resume, name="make_resume"),
path('make_resume1/',make_resume1, name="make_resume1"),
# path('make_pdf/',make_pdf, name="make_pdf"),
# path('make_pdf2/',make_pdf2, name="make_pdf2"),
# path('login/', login_user, name='login'),
# path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# # path('login/', auth_views.LoginView.as_view(), name='login'),
# # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('',index, name="index"),
# path('test_data/',test_data, name="test_data"),
]
