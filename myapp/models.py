import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class CommmonInfo(models.Model):
    only_user_name = models.CharField(max_length=60)
    name = models.CharField(max_length=70)
    dob = models.DateField()
    date = models.DateField()
    father_name = models.CharField(max_length=60)
    mother_name = models.CharField(max_length=60)
    Phone_no = models.IntegerField()
    attendance_date = models.DateField()
    gender = models.CharField(max_length=10)    
    address = models.TextField()
    stud_class = models.CharField(max_length=50)    
    subject_name = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class StudentProfile(CommmonInfo):
    Roll_no = models.IntegerField()
    fees = models.IntegerField()
    date = None
    
class Teacher(CommmonInfo):
    salary = models.IntegerField()

class Contractor(CommmonInfo):
    payment = models.IntegerField()
    stud_class = None
    subject_name= None
    
class StudentMarksheet(models.Model):
    sm_stud_roll = models.IntegerField(unique=True,primary_key=True,null=False)
    sm_name = models.CharField(max_length=70)
    sm_dob = models.DateField()
    sm_date = models.DateField()
    sm_father_name = models.CharField(max_length=60)
    sm_mother_name = models.CharField(max_length=60)
    subject_1 = models.IntegerField()
    subject_2 = models.IntegerField()
    subject_3 = models.IntegerField()
    subject_4 = models.IntegerField()
    subject_5 = models.IntegerField()
    subject_6 = models.IntegerField()
    
