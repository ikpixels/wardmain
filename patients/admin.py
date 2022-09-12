from django.contrib import admin
#from patients.models import User
from patients.models import Doctor,Patient,Ward

 
admin.site.register(Doctor) 
admin.site.register(Patient)
admin.site.register(Ward)

