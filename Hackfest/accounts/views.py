from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from django.contrib.auth.models import User
import uuid
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate
from django.contrib import messages 
from .middleware import auth_middleware


@auth_middleware
def choiseview(request):
    try:

        if request.session['role']== "Admin":
            return render(request, 'choise.html' )
        else:
            return render(request, 'index.html', {'messages': "You Are Not Authenticated"})
    except:
        return render(request, 'index.html', {'messages': "something went wrong!!"})


# @auth_middleware
def doctor_register(request, roledata):
    try:
        if request.method =='POST':
            uname=request.POST.get('uname',None)
            email=request.POST.get('eml',None)
            pwd=request.POST.get('pwd',None)

            if User.objects.filter(username=email).exists():
                messages.add_message(request, messages.ERROR, "User Already Exists")
                return redirect('/accounts/choise/')
            else:
                user_obj=User.objects.create(username=email,password=pwd,email=email)
                user_obj.set_password(pwd)
                user_obj.save()
                if roledata == 'Doctor':
                    role_name = Role.objects.filter(role='Doctor').first()
                    print(role_name.id)
                    userRole= UserroleMap.objects.create(user_id=user_obj, role_id=role_name)
                    userRole.save()
                    messages.add_message(request, messages.SUCCESS, "Doctor is created")
                    return redirect('')
                else:
                   
                    role_name = Role.objects.filter(role='Nurse').first()
            
                    userRole= UserroleMap.objects.create(user_id=user_obj, role_id=role_name)
                    userRole.save()
                    messages.add_message(request, messages.SUCCESS, "Nurse is created")

                    return redirect('')

        return render(request, 'ragister.html', {'messages': 'Please Add Valid Details !'})    
    except Exception as e:
        print("admin")
        print(e)
        return render(request, 'index.html', {'messages': "Something Went Wrong!!"})

@auth_middleware
def addNurse(request):
    try:
        if request.session['role']!= "Admin":
            return render(request, 'index.html', {'messages': "You Are Not Authenticated"})
        data={'roledata': 'Nurse' , 'message': "Register Nurse"}
        return  render(request, 'ragister.html', context= data )
    except:
        print("nurse1")
        return render(request, 'index.html', {'messages': "something went wrong!!"})

@auth_middleware
def addDoctor(request):
    try:
        if request.session['role']!= "Admin":
            return render(request, 'index.html', {'messages': "You Are Not Authenticated"})
        data={'roledata': 'Doctor' , 'message': "Register Doctor"}
        return  render(request, 'ragister.html', context= data )
    except:
        print("nurse2")
        return render(request, 'index.html', {'messages': "something went wrong!!"})


def docter_login(request):
    try:
        if request.method =='POST':
            email=request.POST.get('eml',None)
            pwd=request.POST.get('pwd',None)
            ubj= authenticate(request, username=email, password=pwd) 
            if ubj == None:
                messages.add_message(request, messages.ERROR, "invalid credentials")
                return redirect('/accounts/loginpage')

            q = User.objects.filter(username=email).filter(is_staff=True)
            table1_data= UserroleMap.objects.filter(user_id=ubj.id).first()
            userRole= Role.objects.filter(id=table1_data.role_id.id).first()
            request.session["role"]=userRole.role
            if q and ubj:
                messages.add_message(request, messages.SUCCESS, "Welcome !!")
                return redirect("/accounts/choise/")
            else:

                return render( request, 'doctor.html',  {'msg': "please add valid data !"})

        else:
            return render(request, 'index.html')
    except Exception as e:
        print(e)
        return render(request, 'index.html', {'messages': "Something Went Wrong!!"})

def doctor_logout(request):
    try:
        del request.session['role']
        return redirect('')
    except:
        return HttpResponse('<h3 style="text-align:center"> Somthing went wrong !!!!!</h3>')
