from django.urls import path,include
from . import views

urlpatterns = [
    path('news/',views.NewsData,name='news'),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('newsdate/<int:year>',views.NewsDate,name='NewsDate'),
    path('reg/',views.RegistrationFormData,name='registration'),
    path('adduser/',views.adduser,name='adduser'),
    path('regmodel/',views.RegistrationModelForm,name='modelformcreate'),
    path('regaddmodel/',views.AddUserModelForm,name='modeladduser')



]
