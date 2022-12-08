from http.client import HTTPResponse
import profile
import uuid
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import (ContractorRegistrationAdmin, StudentMarksheetForm,
                    StudentRegistrationAdmin, TeacherRegistrationAdmin)
from .models import (Contractor, Profile, StudentMarksheet, StudentProfile,
                     Teacher)


# Create your views here.
def home(request):
    return render(request, 'home.html')
@login_required(login_url="/login")
def about(request):
    return render(request, 'about.html')
# @login_required(login_url="/login")
def studnet_download(request):
    
     
    # mydata = StudentMarksheet.objects.filter(pk=pk).values()
    # print(mydata)
    # context = {
    # 'mymembers': mydata,
    #     }
    return render(request, 'studentdownloadmarksheet.html')
@login_required(login_url="/login")
def student_mark_sheet_table(request):
    students = StudentMarksheet.objects.all()
    context =  {
        'studss': students,
        }
    return render (request, 'studnetmarksheettable.html', context)


# @login_required(login_url="/login")
def stud_roll_dob(request):
    if request.method == 'POST':
        sm_stud_roll = request.POST.get('sm_stud_roll')
        sm_dob = request.POST.get('sm_dob')
        user_objr = StudentMarksheet.objects.filter(sm_stud_roll = sm_stud_roll).first()
        user_objd = StudentMarksheet.objects.filter(sm_dob = sm_dob).first()
        if user_objr is None:
            messages.success(request, 'Student Roll_NO not found so please try again')
            return redirect('/studrolldob')
        if user_objd is None:
            messages.success(request, 'Student DOB not found so please try again')
            return redirect('/studrolldob')
        
        if sm_stud_roll and sm_stud_roll and sm_dob and sm_dob:
            
            # print(request.POST.get.sm_stud_roll)
            # show = StudentMarksheet.objects.get(pk=sm_stud_roll)
            # current_user = show.sm_name
            # context = {
            #     'show':show
            # }
            tcoder = StudentMarksheet.objects.get(pk=sm_stud_roll)
            total_user = tcoder.subject_1+tcoder.subject_2+tcoder.subject_3+tcoder.subject_4+tcoder.subject_5+tcoder.subject_6
            per=total_user*100/600

            div = ""
            if per >= 60:
                div = "FIRST"
            elif per >= 45:
                div = "SECOND"
            elif per >= 35:
                div = "THIRD"
            else:
                div = "FAIL"
                
            # print(total_user)
            # print(per)
            # print(div)
            show = StudentMarksheet.objects.filter(pk=sm_stud_roll).values()
            # print(show)
            context={
                'show': show,
                'total': total_user,
                'per': per,
                'div': div,
            }
            return render(request, 'studentdownloadmarksheet.html', context)
        else:
            messages.info(request, 'Try again! Techinal issue Student Roll No and DOB')
    
    return render(request, 'student_roll_dob.html')

@login_required(login_url="/login")
def student_mark_sheet(request):
    if request.method=="POST":
        fm = StudentMarksheetForm(request.POST)
        if fm.is_valid():
            sm_stud_roll = fm.cleaned_data['sm_stud_roll']
            sm_name = fm.cleaned_data['sm_name']
            sm_dob = fm.cleaned_data['sm_dob']
            sm_date = fm.cleaned_data['sm_date']
            sm_father_name = fm.cleaned_data['sm_father_name']
            sm_mother_name = fm.cleaned_data['sm_mother_name']
            s1=fm.cleaned_data['subject_1']
            s2=fm.cleaned_data['subject_2']
            s3=fm.cleaned_data['subject_3']
            s4=fm.cleaned_data['subject_4']
            s5=fm.cleaned_data['subject_5']
            s6=fm.cleaned_data['subject_6']
            try:
                if StudentMarksheet.objects.filter(sm_stud_roll=sm_stud_roll).first():
                        messages.success(request, 'Studnet Roll_no is taken.')
                        return redirect('/studentmarksheet')
                reg = StudentMarksheet(sm_stud_roll=sm_stud_roll,sm_name=sm_name,sm_dob=sm_dob,sm_date=sm_date,sm_father_name=sm_father_name,sm_mother_name=sm_mother_name,subject_1=s1,subject_2=s2,subject_3=s3,subject_4=s4,subject_5=s5,subject_6=s6)
                # t=s1+s2+s3+s4+s5+s6
                # p=t*100/500
                reg.save()
                fm = StudentMarksheetForm()
                messages.success(request, 'Student Marksheet succfully created !!')
            except Exception as e:
                messages.success(request, 'something error problem !!   ')
    else:
        fm = StudentMarksheetForm()
    return render(request, 'studentmarksheetdata.html', {'form':fm})
    # return render(request, 'studnetmarksheettable.html',  {'total':t, 'per':p})

###################### Student information data ######################
@login_required(login_url="/login")
def student_show(request):
    if request.method == 'POST':
        fm = StudentRegistrationAdmin(request.POST)
        if fm.is_valid():
            only_user_name = fm.cleaned_data['only_user_name']
            sname = fm.cleaned_data['name']
            sdob = fm.cleaned_data['dob']
            # sdate = fm.cleaned_data['date']
            father_name = fm.cleaned_data['father_name']
            mother_name = fm.cleaned_data['mother_name']
            sstudclass = fm.cleaned_data['stud_class']
            sPhoneno = fm.cleaned_data['Phone_no']
            ssubjectname = fm.cleaned_data['subject_name']
            sgender = fm.cleaned_data['gender']
            sfees = fm.cleaned_data['fees']
            saddress = fm.cleaned_data['address']
            try:
                if len(only_user_name) < 5:
                    messages.success(request, 'username length must be greater than 5 character.')
                    return redirect('/student')
                if not any(char.isdigit() for char in only_user_name):
                    messages.success(request, 'username must contain at isdigit least.')
                    return redirect('/student')
                if not any(char.isalpha() for char in only_user_name):
                    messages.success(request, 'username must contain at isalpha least.')
                    return redirect('/student')
                special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
                if not any(char in special_characters for char in only_user_name):
                    messages.success(request, 'username must contain at special character.')
                    return redirect('/student')
                if StudentProfile.objects.filter(only_user_name=only_user_name).first():
                    messages.success(request, 'name is taken.')
                    return redirect('/student')
                if len(sname) < 5:
                    messages.success(request, 'Name length must be greater than 5 character.')
                    return redirect('/student')
                if len(father_name) < 5:
                    messages.success(request, 'father length must be greater than 5 character.')
                    return redirect('/student')
                if len(mother_name) < 5:
                    messages.success(request, 'mother length must be greater than 5 character.')
                    return redirect('/student')
                if len(saddress) < 5:
                    messages.success(request, 'Address length must be greater than 5 character.')
                    return redirect('/student')


                reg = StudentProfile(only_user_name=only_user_name,name=sname,dob=sdob,father_name=father_name,mother_name=mother_name,stud_class=sstudclass,Phone_no=sPhoneno,subject_name=ssubjectname,gender=sgender,fees=sfees,address=saddress)
                reg.save()
                fm = StudentRegistrationAdmin()
                messages.success(request, 'Student account succfully created !!')
            except Exception as e:
                messages.error(request, str(e))
                

        # else:
        #     messages.success(request, 'Student account not created please try again letter !!')
        #     return redirect('/student')
    else:
        fm = StudentRegistrationAdmin() 
    stud = StudentProfile.objects.all()
    if request.method =="GET":
        st=request.GET.get('searchnamebox')
        if st!=None:
            stud = StudentProfile.objects.filter(name__icontains=st)
            # stud = StudentProfile.objects.filter(Q(name=foo ) | Q(last_name=bar))
    return render(request, 'studentdetails.html', {'stu':stud, 'form':fm})

@login_required(login_url="/login")
def student_update_data(request, id):
    if request.method == 'POST':
        pi = StudentProfile.objects.get(pk=id)
        fm = StudentRegistrationAdmin(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'our account Updated succfully!!')
    else:
        pi = StudentProfile.objects.get(pk=id)
        fm = StudentRegistrationAdmin(instance=pi)
                                             
    return render(request, 'studentupdate.html', {'form':fm})

@login_required(login_url="/login")
def student_delete_data(request, id):
    if request.method == 'POST':
        pi = StudentProfile.objects.get(pk=id)
        pi.delete()
    return redirect('/student')
###################### Student information data ######################

###################### Teacher information data ######################

@login_required(login_url="/login")
def teacher_show(request):
    if request.method == 'POST':
        fm = TeacherRegistrationAdmin(request.POST)
        if fm.is_valid():
            only_user_name = fm.cleaned_data['only_user_name']
            tname = fm.cleaned_data['name']
            tdob = fm.cleaned_data['dob']
            tdate = fm.cleaned_data['date']
            father_name = fm.cleaned_data['father_name']
            mother_name = fm.cleaned_data['mother_name']
            tstudclass = fm.cleaned_data['stud_class']
            tPhoneno = fm.cleaned_data['Phone_no']
            tsubjectname = fm.cleaned_data['subject_name']
            tattendancedate = fm.cleaned_data['attendance_date']
            tgender = fm.cleaned_data['gender']
            tsalary = fm.cleaned_data['salary']
            taddress = fm.cleaned_data['address']
            try:
                if len(only_user_name) < 5:
                    messages.success(request, 'username length must be greater than 5 character.')
                    return redirect('/teacher')
                if not any(char.isdigit() for char in only_user_name):
                    messages.success(request, 'username must contain at isdigit least.')
                    return redirect('/teacher')
                if not any(char.isalpha() for char in only_user_name):
                    messages.success(request, 'username must contain at isalpha least.')
                    return redirect('/teacher')
                special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
                if not any(char in special_characters for char in only_user_name):
                    messages.success(request, 'username must contain at special character.')
                    return redirect('/teacher')
                if Teacher.objects.filter(only_user_name = only_user_name).first():
                    messages.success(request, 'username is taken.')
                    return redirect('/teacher')
                if len(father_name) < 5:
                    messages.success(request, 'father length must be greater than 5 character.')
                    return redirect('/teacher')
                if len(mother_name) < 5:
                    messages.success(request, 'mother length must be greater than 5 character.')
                    return redirect('/teacher')
                if len(tname) < 5:
                    messages.success(request, 'Name length must be greater than 5 character.')
                    return redirect('/teacher')
                
                if len(taddress) < 5:
                    messages.success(request, 'Address length must be greater than 5 character.')
                    return redirect('/teacher')

                # if len(tPhoneno) < 10:
                #     messages.success(request, 'Phone number length must be greater than 10 character.')
                #     return redirect('/contractor')
               
                reg = Teacher(only_user_name=only_user_name,name=tname,dob=tdob,date=tdate,father_name=father_name,mother_name=mother_name,stud_class=tstudclass,Phone_no=tPhoneno,subject_name=tsubjectname,attendance_date=tattendancedate,gender=tgender,salary=tsalary,address=taddress)
                reg.save()
                fm = TeacherRegistrationAdmin()
                messages.success(request, 'Teacher account succfully created !!')
            except Exception as e:
                messages.error(request, str(e))
        # else:
        #     messages.success(request, 'Teacher account not created please try again letter !!')
        #     return redirect('/teacher')
    else:
        fm = TeacherRegistrationAdmin() 
    tstud = Teacher.objects.all()
    if request.method =="GET":
        st=request.GET.get('searchnamebox')
        if st!=None:
            tstud = Teacher.objects.filter(name__icontains=st)
    return render(request, 'teacherdetails.html', {'tstu':tstud, 'form':fm})


@login_required(login_url="/login")
def teacher_update_data(request, id):
    if request.method == 'POST':
        pi = Teacher.objects.get(pk=id)
        fm = TeacherRegistrationAdmin(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'our account Updated succfully!!')
    else:
        pi = Teacher.objects.get(pk=id)
        fm = TeacherRegistrationAdmin(instance=pi)
                                             
    return render(request, 'teacherupdate.html', {'form':fm})

@login_required(login_url="/login")
def teacher_delete_data(request, id):
    if request.method == 'POST':
        pi = Teacher.objects.get(pk=id)
        pi.delete()
    return redirect('/teacher')
###################### teacher information data ######################

###################### contractor information data ######################
@login_required(login_url="/login")
def contractor_show(request):
    if request.method == 'POST':
        fm = ContractorRegistrationAdmin(request.POST)
        if fm.is_valid():
            only_user_name = fm.cleaned_data['only_user_name']
            sname = fm.cleaned_data['name']
            sdob = fm.cleaned_data['dob']
            sdate = fm.cleaned_data['date']
            father_name = fm.cleaned_data['father_name']
            mother_name = fm.cleaned_data['mother_name']
            Phoneno = fm.cleaned_data['Phone_no']
            sattendancedate = fm.cleaned_data['attendance_date']
            sgender = fm.cleaned_data['gender']
            spayment = fm.cleaned_data['payment']
            saddress = fm.cleaned_data['address']
            try:
                if len(only_user_name) < 5:
                    messages.success(request, 'username length must be greater than 5 character.')
                    return redirect('/contractor')
                if not any(char.isdigit() for char in only_user_name):
                    messages.success(request, 'username must contain at isdigit least.')
                    return redirect('/contractor')
                if not any(char.isalpha() for char in only_user_name):
                    messages.success(request, 'username must contain at isalpha least.')
                    return redirect('/contractor')
                special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
                if not any(char in special_characters for char in only_user_name):
                    messages.success(request, 'username must contain at special character.')
                    return redirect('/contractor')
                if Contractor.objects.filter(only_user_name = only_user_name).first():
                    messages.success(request, 'username is taken.')
                    return redirect('/contractor')

                if len(father_name) < 5:
                    messages.success(request, 'father length must be greater than 5 character.')
                    return redirect('/contractor')
                if len(mother_name) < 5:
                    messages.success(request, 'mother length must be greater than 5 character.')
                    return redirect('/contractor')
                if len(sname) < 5:
                    messages.success(request, 'Name length must be greater than 5 character.')
                    return redirect('/contractor')
                
                if len(saddress) < 5:
                    messages.success(request, 'Address length must be greater than 5 character.')
                    return redirect('/contractor')
                

                reg = Contractor(only_user_name=only_user_name,name=sname,dob=sdob,father_name=father_name,mother_name=mother_name,date=sdate,Phone_no=Phoneno,attendance_date=sattendancedate,gender=sgender,payment=spayment,address=saddress)
                reg.save()
                messages.success(request, 'Contractor account succfully created !!')
                return redirect('/contractor')
            except Exception as e:
                messages.error(request, str(e))
    else:
        fm = ContractorRegistrationAdmin() 
    stud = Contractor.objects.all()
    if request.method =="GET":
        st=request.GET.get('searchnamebox')
        if st!=None:
            stud = Contractor.objects.filter(name__icontains=st)
    return render(request, 'contractordetails.html', {'stu':stud, 'form':fm})

@login_required(login_url="/login")
def contractor_update_data(request, id):
    if request.method == 'POST':
        pi = Contractor.objects.get(pk=id)
        fm = ContractorRegistrationAdmin(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'our account Updated succfully!!')
    else:
        pi = Contractor.objects.get(pk=id)
        fm = ContractorRegistrationAdmin(instance=pi)
                                             
    return render(request, 'contractorupdate.html', {'form':fm})

@login_required(login_url="/login")
def contractor_delete_data(request, id):
    if request.method == 'POST':
        pi = Contractor.objects.get(pk=id)
        pi.delete()
    return redirect('/contractor')
###################### Contractor information data ######################

def login_attempt(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username = username).first()
            if user_obj is None:
                messages.success(request, 'User not found so please create a new account')
                return redirect('/login')

            profile_obj = Profile.objects.filter(user = user_obj).first()

            if not profile_obj.is_verified:
                messages.success(request, 'Profile is not verified check your mail.')
                return redirect('/login')
            user = authenticate(username = username, password = password)
            if user is None:
                messages.success(request, 'wrong username and password')
                return redirect('/login')
            
            login(request, user)
            return redirect('/')
        return render(request, 'login.html')
    else:
        return redirect('/')

def register_attempt(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            try:
                if User.objects.filter(username = username).first():
                    messages.success(request, 'Username is taken.')
                    return redirect('/register')

                if User.objects.filter(email = email).first():
                    messages.success(request, 'email is taken.')
                    return redirect('/register')

                # pasword generator method validation error
               
                if len(password) < 8:
                    messages.success(request, 'Password length must be greater than 8 character.')
                    return redirect('/register')
                if not any(char.isdigit() for char in password):
                    messages.success(request, 'Password must contain at isdigit least.')
                    return redirect('/register')
                if not any(char.isalpha() for char in password):
                    messages.success(request, 'Password must contain at isalpha least.')
                    return redirect('/register')
                special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
                if not any(char in special_characters for char in password):
                    messages.success(request, 'Password must contain at special character.')
                    return redirect('/register')
                user_obj = User(username = username , email = email)
                user_obj.set_password(password)
                user_obj.save()
                
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
                profile_obj.save()
                send_mail_after_registration(email , auth_token)
                messages.success(request, 'we have send as email to you | please check your mail')
                return redirect('/login')
            except Exception as e:
                print(e)
                messages.success(request, 'Your Email ID Internet Connection Not Matching please try again letter !!')

        return render(request, 'register.html')
    else:
        return redirect('/')
@login_required(login_url="/login")
def logout_view(request):
    logout(request)
    return redirect('/login')

  
def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()

        if profile_obj:
            
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/login')
        else:
            messages.success(request, 'please try again letter | not matching verified mail')
    except Exception as e:
        print(e)
        return redirect('/')


def send_mail_after_registration(email , token):

    subject = 'Your account need to be verified'
    message = f'how are better   said past the link to verify your account http://127.0.0.1:8000/verify/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    