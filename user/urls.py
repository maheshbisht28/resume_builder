from django.urls import path, include
from django.conf.urls import url
from  .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
path('login/', login_user, name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
url(r'^oauth/', include('social_django.urls', namespace='social')),

]
