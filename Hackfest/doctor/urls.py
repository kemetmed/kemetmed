
from django.urls import path
from . import views

urlpatterns = [
    path('/loginpg' , views.docter_login),
    path('/logout' , views.doctor_logout),
    path('patient-list/', views.patientList)
]
