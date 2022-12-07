from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from .models import Prescription, PrescribedMedicine, Medicine
from healthcare.models import Patient, PatientRecord
from django.contrib.auth.models import User
from .helpers import *
import uuid
from .models import Profile
from django.contrib.auth import authenticate

# Create your views here.


def docter_login(request):
    try:
        if request.method =='POST':
            uname=request.POST.get('uname',None)
            pwd=request.POST.get('pwd',None)
            ubj= authenticate(request,username=uname,password=pwd)
            
            if ubj:
                return HttpResponse("Logged in...")
            else:
                return HttpResponse("Invalid creadentials...")

        else:
            return render(request, 'index.html')

    except:
        return HttpResponse("<h3>Somthing is wrong !!!!!</h3>")
    #  vlidate session use this if request.session.has_key('uid'):
    #     return HttpResponse("Logged in...")

def doctor_logout(request):
    try:
        del request.session['uid']
        return redirect('/doctor/loginpage')
    except:
        return HttpResponse("<h3>Somthing is wrong !!!!!</h3>")
#Patients List 
def patientList(request):
    data = Patient.objects.all()
    return render(request, "patientlist.html", {'data':data})   



def forgot_password(request):
    try:
        return render(request, 'otp.html')
    except:
        return HttpResponse("something went wrong !!!!!!!")   


# def forgot_user_validate(request):
#     try:
#         data=request.POST.get('uname',None)
#         return render(request, 'otppage.html', {"labels":data}) 
#     except:
#         return HttpResponse("something went wrong !!!!!!!")   




def ForgetPassword(request):
    
    if request.method=='POST':
        username=request.POST.get('uname', None)
        if not User.objects.filter(username=username).first():
            return HttpResponse('No user found')
        user_obj= User.objects.get(username=username)
        profile_obj= Profile.objects.filter(user = user_obj).first()
        if profile_obj == None:
            profile_obj = Profile.objects.create(user = user_obj )
            profile_obj.save()

        token = str(uuid.uuid4())
        

        profile_obj.forget_password_token = token
        profile_obj.save()
        send_forget_password_mail(user_obj.email ,token)
        
        return HttpResponse('email is sent!!!!!')
            
    # except:
    #     return HttpResponse('something went wrong')

# def changepassword(request , token):
#     context = {}
    
    
    
#     profile_obj = Profile.objects.filter(forget_password_token = token).first()
#     context = {'user_id' : profile_obj.user.id}
        
#     if request.method == 'POST':
#         new_password = request.POST.get('pwd')
#         confirm_password = request.POST.get('cpwd')
#         user_id = request.POST.get('user_id')
            
#         if user_id is  None:
#             return redirect(f'/change-password/{token}/')
                
            
#         if  new_password != confirm_password:
#             return redirect(f'/change-password/{token}/')
                         
            
#         user_obj = User.objects.get(id = user_id)
#         user_obj.set_password(new_password)
#         user_obj.save()
#         return redirect('/login/')
#     # except:
#     #     return HttpResponse("not done")



# def changepassword(request, token):
#     return render(request,'changepassword.html', {"token":token})


# def changepassword(request, token):
#     if request.method == 'POST':
#         profile_obj = Profile.objects.filter(forget_password_token = token).first()
#         new_password = request.POST.get('pwd')
#         return HttpResponse('new response')
#     return render(request,'changepassword.html', {"token":token})

def makeprescriptions(request):
    if request.method == 'POST':
        patientId = request.session.get('id')
        patient = Patient.objects.get(patientId=patientId)
        prescriptionsDate = request.POST["date"]
        priscription = Prescription(prescriptionIssueDate=prescriptionsDate,prescriptionPatient=patient)
        priscription.save()
        return render(request, "",{"data":priscription})

def addMedicineOnPrescription(request):
    if request.method=="POST":
        prescribedMedicineDuration=request.POST['prescribedMedicineDuration']
        prescribedMedicineMedicine=request.POST['medicineId']
        prescribedMedicineQuantity=request.POST['prescribedMedicineQuantity']
        prescribedMedicineTakenQuantity=request.POST['prescribedMedicineTakenQuantity']
        prescribedMedicinePrescription=request.POST['prescriptionId']
        prescribedMedicineDiagnosis= request.POST['prescriptionDiagnosis']
        medicine = Medicine.objects.get(medicineId=prescribedMedicineMedicine)
        prescription = Prescription.objects.get(prescriptionId=prescribedMedicinePrescription)

        prescribedMedicine = PrescribedMedicine(prescribedMedicineDuration=prescribedMedicineDuration,prescribedMedicineMedicine=medicine,prescribedMedicineQuantity=prescribedMedicineQuantity,prescribedMedicineTakenQuantity=prescribedMedicineTakenQuantity,prescribedMedicineDiagnosis=prescribedMedicineDiagnosis,prescribedMedicinePrescription=prescription)
        prescribedMedicine.save()
        return HttpResponse("added")

def seePrescription(request):
    patientId = request.session.get('id')
    return render(request, "Patient/patient_prescription.html")


def getPrescriptionsOnId(request):
    if request.method == "GET":
        patientId = request.session.get('id')
        prescriptions = Prescription.objects.raw("select prescriptionId from doctor_prescription inner join healthcare_patient on healthcare_patient.patientId=doctor_prescription.prescriptionPatient where patientId='"+str(patientId)+"'")
        return render(request, "Patient/prescription.html", {"data": prescriptions})


def getPrescriptionMedicineOnId(request):
    if request.method == "GET":
        prescriptionId = request.GET['prescriptionId']
        prescription = Prescription.objects.get(prescriptionId=prescriptionId)
        prescriptionMedicines = PrescribedMedicine.objects.filter(
            prescribedMedicinePrescription=prescription)
        return render(request, "Patient/prescription.html", {"data": prescriptionMedicines})


def addMedicineOnId(request):
    if request.method == "GET":
        medicineId = request.GET['medicineId']
        medicineName=request.POST['medicineName']
        signleUnitQuantity=request.POST['signleUnitQuantity']
        medicine = Medicine(medicineId=medicineId,medicineName=medicineName,signleUnitQuantity=signleUnitQuantity)
        return render(request, "medicine.html", {"data": medicine})


# def getPrescribedMedicineMedicineOnId(request):
#     if request.method == "GET":
#         prescribedMedicineId = request.GET['prescribedMedicineId']
#         prescribedMedicineMedicien = Medicine.objects.filter(
#             prescribedmedicine__prescribedMedicineId=prescribedMedicineId)
#         data = {
#             "prescribedMedicineMedicien": list(prescriptions.values())
#         }
#         return HttpResponse(json.dumps(data))

        
