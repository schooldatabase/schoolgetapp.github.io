from django.contrib import admin
from .models import Profile, StudentMarksheet, StudentProfile, Teacher, Contractor
# Register your models here.

admin.site.register(Profile)
# admin.site.register(Show)
# admin.site.register(StudentMarksheet)

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'only_user_name', 'name', 'dob', 'date', 'father_name', 'mother_name', 'stud_class', 'Phone_no','gender', 'fees', 'address']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','only_user_name', 'name', 'dob', 'father_name', 'mother_name', 'stud_class', 'Phone_no', 'subject_name', 'attendance_date', 'gender', 'address', 'date', 'salary']

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['id', 'only_user_name', 'name', 'date', 'father_name', 'mother_name', 'Phone_no', 'attendance_date', 'gender', 'address', 'payment']


@admin.register(StudentMarksheet)
class StudentMarksheetForm(admin.ModelAdmin):
    list_display = "__all__"
      
    list_display = ['sm_stud_roll',  'sm_name', 'sm_dob', 'sm_father_name', 'sm_mother_name','subject_1','subject_2','subject_3','subject_4','subject_5','subject_6']