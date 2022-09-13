from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.views.generic import ListView, DetailView,CreateView
from .models import Patient,Doctor,Ward
from django.contrib import messages
from django.db.models import Q



def patient_view(request,id=None):#main dashboard

    context = {}

    if id:
        context['Patient'] = Patient.objects.get(id=id)
    else:
        context['Patient'] = Patient.objects.all().last()

    return render(request,'patients.html',context)


def patient_list(request):
    context = {}
    context['Patient'] = Patient.objects.all()
    return render(request,'patients_list.html',context)

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
  