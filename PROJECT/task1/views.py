from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import User,Doctor, Patient
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        context = {"details":user}
        if user.is_patient==True:
            return render(request,'patienthome.html',context=context)
        if user.is_doctor==True:
            return render(request,"doctorhome.html",context=context)
        else:
            return render(request,"home.html")
    else:
        messages.warning(request,"Login & Try Again")
        return redirect('/signin')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/home")
            else:
                return redirect("/signin")
        else:
            return render(request,"login.html")

def doctorsignup(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            confpassword = request.POST['confirmpassword']
            if password==confpassword:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                login(request,user)
                user = User.objects.get(username=username)
                email = request.POST['email']
                user.is_doctor=True
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                user.email=email
                user.first_name=firstname
                user.last_name=lastname
                user.save()
                profilepic = request.FILES['pic']
                adrs = request.POST['line1']
                city = request.POST['city']
                state = request.POST['state']
                pincode = request.POST['pincode']
                doc = Doctor(user=request.user,profilepic=profilepic,line1 = adrs ,city =city,state=state,pincode=pincode)
                doc.save()
                messages.success(request,"Signup Successful, plz..login")
                return redirect('/')
            else:
                messages.warning(request,"Something went wrong") 
                return redirect('/signup/doctor')
        else: 
            messages.warning(request,"Something went wrong")  
            return render(request,"doctorsignup.html")
        
def patientsignup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            confpassword = request.POST['confirmpassword']
            if password==confpassword:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                login(request,user)
                user = User.objects.get(username=username)
                email = request.POST['email']
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                user.is_patient=True
                user.email=email
                user.first_name=firstname
                user.last_name=lastname
                user.save()
                profilepic = request.FILES['pic']
                adrs = request.POST['line1']
                city = request.POST['city']
                state = request.POST['state']
                pincode = request.POST['pincode']
                doc = Doctor(user=request.user,profilepic=profilepic,line1 = adrs ,city =city,state=state,pincode=pincode)
                doc.save()
                messages.success(request,"Signup Successful, plz..login")
                return redirect('/')
            else:
                messages.warning(request,"Something went wrong") 
                return redirect('/signup/patient')
        else:  
            messages.warning(request,"Something went wrong")  
            return render(request,"patientsignup.html")

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Signout Successfully")
        return redirect("/signin")
    else:
        return redirect('/')