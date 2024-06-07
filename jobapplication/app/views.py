from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .forms import UserRegisterForm,LoginForm,EmployeeBasicDetailsForms
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib.auth import logout
from .utils import session_login_required



def RegistrationFormData(request):
    context={
        "form":UserRegisterForm()
    }
    return render(request,'register.html',context)


def AddUserModelForm(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('loginform')
        else:
            msg = 'form is not valid'
    else:
        form = UserRegisterForm()
    return render(request,'register.html', {'form': form})
   

def LoginFormData(request):
    if request.session.get('username'):
        return redirect('home')
    context={
        "form":LoginForm()
    }
    return render(request,'login.html',context)

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('loginform')
        user = auth.authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('loginform')
        else:
            login(request, user)
            request.session['username'] = username
            request.session.save()
            return redirect('home')
    else:
        form = LoginForm()
     
    return render(request, 'login.html',{'form':form})

def signout(request):
    logout(request)
    return redirect('loginform')


# @session_login_required
# def EmployeeBasicDetailsView(request):
#     if request.method=="GET":
#         context={
#             "form":EmployeeBasicDetailsForms()
#         }
#         return render(request,'job.html',context)
    

@session_login_required
def home(request):
    if request.method=="GET":
        context={
            "form":EmployeeBasicDetailsForms()
        }
        return render(request,'job.html',context)