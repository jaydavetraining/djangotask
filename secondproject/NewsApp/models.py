from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class News(models.Model):
    author=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    description=models.TextField()
    pub_date=models.DateField(default=timezone.now())

    def __str__(self):
        return self.author
    
class RegistrationForm(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)

    def __str__(self):
        return self.username


# abstrct model class

class ContactInfo(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    address=models.CharField(max_length=200)

    class Meta:
        abstract = True

class Customer(ContactInfo):
    phone=models.CharField(max_length=30)

class Staff(ContactInfo):
    position=models.CharField(max_length=30)



class MyNewUser(User):
    class Meta:
        ordering = ('username',)
        proxy = True

    def fullName(self):
        return self.first_name + "" + self.last_name