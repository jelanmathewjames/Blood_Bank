from django.shortcuts import render, redirect
from Blood_bank_app.models import DonorDetails
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def home(request):
    return redirect('login')


def log_in(request):

    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("display")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'blood_login.html')

    
def sign_in(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('signin')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('signin')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,password=password1,username=username,email=email)
                user.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching...')
            return redirect(request,'signin')
    else: 
        return render(request,'blood_signup.html')


def display(request):

    details = DonorDetails.objects.all()
    return render(request,'Blood_data.html',{'data':details})


def adddonor(request):

    if request.method == 'POST':
        name = request.POST['name']
        blood_group = request.POST['blood_group']
        age = request.POST['age']
        phone_number = request.POST['phone_number']
        details = DonorDetails.objects.create(name=name,blood_group=blood_group,age=age,phone_number=phone_number)
        details.save()
        return redirect('display')
    else:
        return render(request, 'Blood_home.html')


def logout(request):
    
    auth.logout(request)
    return redirect('login')