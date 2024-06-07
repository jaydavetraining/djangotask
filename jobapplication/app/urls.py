from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('',views.RegistrationFormData,name='Register'),
    path('adduser/',views.AddUserModelForm,name='Adduser'),
    path('loginform/',views.LoginFormData,name='loginform'),
    path('login/',views.sign_in,name='login'),
    path('logout/',views.signout,name='logout'),



]