from django.shortcuts import render, redirect
from Blood_bank_app.models import DonorDetails
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def home(request):
    return redirect('login')


def log_in(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            request.session['session_valid'] = username
            return JsonResponse(
                {'success':True},
                safe = False
            )
        else:
            return JsonResponse(
                {'success':False},
                safe = False
            )
    else:
        return render(request,'blood_login.html')

    
def sign_up(request):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
    
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    return JsonResponse(
                        {'success':'user_error'},
                        safe = False
                    )
                elif User.objects.filter(email=email).exists():
                    return JsonResponse(
                        {'success':'email_error'},
                        safe = False
                    )
                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,password=password1,username=username,email=email)
                    user.save()
                    return JsonResponse(
                        {'success':'True'},
                        safe = False
                    )
            else:
                return JsonResponse(
                    {'success': 'password_error'},
                    safe = False
                )
        else: 
            return render(request,'blood_signup.html')


def display(request):
    if 'session_valid' in request.session :
        details = DonorDetails.objects.all()
        return render(request,'Blood_data.html',{'data':details})


def adddonor(request):
    if 'session_valid' in request.session :
        if request.method == 'POST':
            name = request.POST['name']
            blood_group = request.POST['blood_group']
            age = request.POST['age']
            phone_number = request.POST['phone_number']
            if DonorDetails.objects.filter(phone_number=phone_number).exists():
                return JsonResponse(
                    {'success':'phonenumber_error'},
                    safe = False
                )
            elif DonorDetails.objects.filter(name=name).exists():
                return JsonResponse(
                    {'success':'name_error'},
                    safe = False
                )
            else:
                details = DonorDetails.objects.create(name=name,blood_group=blood_group,age=age,phone_number=phone_number)
                details.save()
                return JsonResponse(
                    {'success':'true'},
                    safe = False
                )
        else:
            return render(request, 'Blood_home.html')


def logout(request):
    if 'session_valid' in request.session :
        try:
            del request.session['session_valid']
        except KeyError:
            pass
        return redirect('login')