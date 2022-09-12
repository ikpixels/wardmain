from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.IntegerField()
    specialisation=models.TextField()
    
    def _str_(self): 
       return self.name

class Ward(models.Model):
    name=models.CharField(max_length=100)
    number_of_beds=models.IntegerField()
    def _str_(self):
        return self.name


class Patient(models.Model): 
    id_number=models.IntegerField()
    first_name=models.CharField(max_length=100, blank=True)
    last_name=models.CharField(max_length=150, blank=True)
    email=models.EmailField()
   # patient_gurdians_phone_number=models.IntegerField()
    date_of_birth=models.DateField() 
    temperature=models.DecimalField(max_digits=4, decimal_places=1)
    heart_rate=models.IntegerField()
    status = models.CharField(max_length=100,default="pending")
    pulse_oxymetry=models.DecimalField(max_digits=2, decimal_places=2)
    doctor=models.ForeignKey(Doctor,on_delete =models.PROTECT)
    ward=models.ForeignKey(Ward, on_delete=models.PROTECT)
    
    def _str_(self):
       return self.first_name+''+ self.last_name






def get_absolute_url(self):
    return reverse("people-detail",kwargs={"pk":self.pk})
     


    

    







