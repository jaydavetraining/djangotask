from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import News,RegistrationForm
from .forms import RegistrationFormsUser,RegistarionModelformUser
from django.contrib import messages
# Create your views here.


def NewsDate(request,year):
    print(year,type(year))
    artical_list=News.objects.filter(pub_date__year=year)
    con={
        'year':year,
        'artical_list':artical_list
    }
    return render(request,'newsdate.html',con)


def NewsData(request):
    data=News.objects.get(id=1)
    print(data.description)
    context={
        # "list":['python','php','c#','kotlin','android','java'],
        # "mynum":50
        "data":data

    }
    return render(request,'news.html',context)

def home(request):
    context={
        "name":"jay dave",
        "number":12312
    }
    return render(request,'home.html',{'context':context})

def contact(request):
    return render(request,'contact.html')

def RegistrationFormData(request):
    context={
        "form":RegistrationFormsUser
    }
    return render(request,'reg.html',context)


def adduser(request):
    form=RegistrationFormsUser(request.POST)
    if form.is_valid():
        register=RegistrationForm(username=form.cleaned_data['username'],password=form.cleaned_data['password'],email=form.cleaned_data['email'],phone=form.cleaned_data['phone'])
        register.save()
        messages.add_message(request,messages.SUCCESS,"you have signup successfully")
        print(messages,"++++++",messages.SUCCESS)
    return redirect('registration')

def RegistrationModelForm(request):
    context={
        "modelform":RegistarionModelformUser
    }
    return render(request,'modelform.html',context)


def AddUserModelForm(request):
    form=RegistarionModelformUser(request.POST) 
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"you have signup successfully")
        print(messages,"++++++",messages.SUCCESS)
    return redirect('modelformcreate')