from django.shortcuts import render




# Create your views here.


from django.http import HttpResponse
import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.urls import reverse


def login_user(request):
    email = password = ''
    print("here")
    if request.POST:
        user_email = request.POST.get('user_email')
        password1 = request.POST.get('password1')
        print(user_email)
        print(password1)
        # print(request.POST)

        user = authenticate(email=user_email, password=password1)
        print(user)
        if user:
            print(user.is_active)
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
        	return HttpResponseRedirect(reverse('index'))


    # return render('login.html',{'username': username}, context_instance=RequestContext(request))
    return render(request,'index1.html')