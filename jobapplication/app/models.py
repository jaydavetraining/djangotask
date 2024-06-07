from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone=models.CharField(max_length=14) 
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username


class EmployeeBasicDetails(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)    
    designation=models.CharField(max_length=100)
    phone=models.IntegerField()
    gender=models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    relationship_status=models.CharField(max_length=20)
    address1=models.TextField()
    address2=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    birthday=models.DateField(auto_now=False)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.id - self.first_name}'

class EducationDetail(models.Model):
    boardname=models.CharField(max_length=50)
    university=models.CharField(max_length=50)
    passingyear=models.IntegerField()
    passingyear=models.FloatField()
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

class WorkExperience(models.Model):
    compname=models.CharField(max_length=200)
    designation=models.CharField(max_length=100)
    durationfrom=models.DateField(auto_now=False)
    durationto=models.DateField(auto_now=False)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

class LanguageMaster(models.Model):
    lanvalue=models.CharField(max_length=50)
    readfluency=models.BooleanField()
    writefluency=models.BooleanField()
    speakfluency=models.BooleanField()
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

class TechnologyMaster(models.Model):
    techalue=models.CharField(max_length=50)
    techproficiency=models.BooleanField()
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

class ReferenceContact(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField(null=True,blank=True)
    relation=models.CharField(max_length=50)   
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

class preferences(models.Model):
    preferencelocation=models.CharField(max_length=50)
    noticeperiod=models.IntegerField(null=True,blank=True)
    expectedctc=models.FloatField(null=True,blank=True)
    currentctc=models.FloatField(null=True,blank=True)
    department=models.CharField(null=True,blank=True)



    


