# Create your views here.
from django.shortcuts import render, redirect
from .models import ApplicationModel
from django.core.files.storage import FileSystemStorage
from django.views.generic import DetailView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#-------------------------------------------------------------------------------------
#============================ Function To Post Form Data===============================================
def form_view(request):
    if request.method == 'POST':
        Name = request.POST['name']
        Email = request.POST['email']
        Phone = request.POST['phone']
        Choice = request.POST.getlist('catagory')
        CvUpload = request.FILES['myFile']
        fs=FileSystemStorage(location='media')
        fn=fs.save(CvUpload.name,CvUpload)
        Motivation = request.POST['motivation']
        downloadCv = fs.url(fn)
        applicationModel_obj = ApplicationModel(name=Name, email=Email, phone=Phone, catagory=Choice, CvResume=CvUpload,
                                                motivation=Motivation)

        applicationModel_obj.save()
        return redirect('form')
    return render(request, 'form.html')
#-------------------------------------------------------------------------------------
#=======================Function To View All Data======================================================

@login_required()
def displayData_view(request):
    allData_obj = ApplicationModel.objects.all()
    allData_dict = {'allDataKey': allData_obj}
    return render(request, 'index.html', allData_dict)
#-------------------------------------------------------------------------------------
#=======================Function To View Applicant Details=============================================
@login_required()
class ApplicationModelDetailView(DetailView):
    model = ApplicationModel
    template_name = 'detail.html'
    context_object_name = 'applicant'
#-------------------------------------------------------------------------------------
#=======================Function to Delete a Applicant Data============================================
@login_required()
def deleteData_view(request,id):
    delData_obj=ApplicationModel.objects.get(pk=id)
    delData_obj.delete()
    return redirect('home')
#-------------------------------------------------------------------------------------
#=======================Functions For Login and Logout=================================================
def login_view(request):
    return redirect(request,'login.html')

def logout_view(request):
    logout(request)
    return render(request,'login.html')
#-------------------------------------------------------------------------------------
#======================Function To Register New User=======================================================
@login_required()
def register_view(request):
    if request.method=='POST':
        Username=request.POST["RegisterUsername"]
        Password=request.POST["RegisterPassword"]
        Email=request.POST["RegisterEmail"]
        user_obj=User.objects.create_user(username=Username,password=Password,email=Email)
        user_obj.save()
        return redirect('register')
    else:
        return render(request,'register.html')
