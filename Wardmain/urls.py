from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from patients import views #importing views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.patient_view,name=''),
    path('doctor/',views.doctor,name="doctor"),
    path('patient_list/',views.patient_list,name="patient_list"),
    path('patient/<int:id>/',views.patient_view,name='patient_deteil'),
  
    
    
] 

urlpatterns+=staticfiles_urlpatterns()

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 