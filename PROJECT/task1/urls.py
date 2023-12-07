from django.urls import path
from task1.views import signin,doctorsignup,home,patientsignup,signout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home),
    path('home', home),
    path('signin', signin),
    path('signup/doctor', doctorsignup),
    path('signup/patient', patientsignup),
    path('signout/', signout),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)