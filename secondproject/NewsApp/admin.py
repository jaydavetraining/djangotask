from django.contrib import admin

# Register your models here.
from .models import News,RegistrationForm,Customer,Staff,MyNewUser

admin.site.register(News)
admin.site.register(RegistrationForm)
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(MyNewUser)
