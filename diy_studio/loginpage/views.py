from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from.models import Registration

# Create your views here.
def webpage(request):
    return render(request,'webpage.html')

def register(request):
    uform = UserCreationForm(request.POST)
    if request.method == "POST":
        if uform.is_valid():
            uname = uform.cleaned_data.get('username')
            pwd = uform.cleaned_data.get('password1')
            email = uform.cleaned_data.get('email')
            user1 = User.objects.create_user(username=uname, password=pwd, email=email)
            user1.save()
            user = authenticate(request, username=uname, password=pwd)
            login(request, user)
            return redirect('/loginpage/login/')
    else:
        uform = UserCreationForm()
    return render(request,'registartion.html',{'form':uform})







def login0(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/loginpage/webpage/')
        else:
            return HttpResponse("Username or Password is incorrect")
    return render(request, 'login0.html')

def products(request):
    return render(request,'products.html')

def single(request):
    return render(request, 'single products.html')


