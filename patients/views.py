from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.views.generic import ListView, DetailView,CreateView
from .models import Patient,Doctor,Ward
from django.contrib import messages

def patient_view(request):#main dashboard

    context = {}

    context['Patient'] = Patient.objects.all()#patient list

    context['Patient_c'] = Patient.objects.all().count()#getting total number of patients
    context['doctor_c']= Doctor.objects.all().count()#getting total number of doctor
    context['ward_c']= Ward.objects.all().count()#getting total number of ward
    
    return render(request,'patients.html',context)

def patient_deteil_view(request,id):
    context = {}
    context['Patient'] = Patient.objects.get(id=id)
    return render(request,'patient_deteil.html',context)

def doctor(request):
    context = {}
    context['doctor'] = Patient.objects.all()
    return render(request,'doctor.html',context)
                                  
def register(request):
    if request.method=='POST':
        first_name=request.POST[first_name]
        last_name=request.POST[last_name]
        email=request.POST[email]
        password1=request.POST[password1]
        password2=request.POST[password2]

        user=User.objects.create_user(password=password1,email=email,first_name=first_name,last_name=last_name,)
        user.save();
        print("user created")
        return redirect('/')
    else:

        return render(request,'form.html')
  