from django.shortcuts import render,redirect,HttpResponse

from blog.models import Blog, Blogform
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def login_blog(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Wrong email or password')

    return render(request, 'account/login.html')

def register_blog(request):
    if request.method == 'POST':
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        phone_no=request.POST['contact']
        profile=request.FILES['profile_pic']
        if password1!=password2:
            messages.add_message(request,messages.ERROR,'Passwords do not match')
            return redirect('register')

        elif password1=='' or password2=='':
            messages.add_message(request, messages.ERROR, "Passwords can't be empyty")
            return redirect('register')

        else:
            CustomUser.objects.create_user(email=email, password=password1, phone_no=phone_no, profile_picture=profile)
            return redirect('login')


    else:

        return render(request, 'account/register.html')


def logout_blog(request):
    logout(request)
    return redirect('home')



