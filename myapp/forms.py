from django import forms
from django.forms import ValidationError
from .models import StudentMarksheet, StudentProfile, Teacher, Contractor
from django.core.validators import RegexValidator

# class StudentRegistration(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['name', 'email', 'password']
#         widgets = {'name' : forms.TextInput(attrs={'class':'form-control'}),
#             'email' : forms.EmailInput(attrs={'class':'form-control'}),
#             'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),}

class HTML5DateWidget(forms.widgets.Input):
    input_type = 'date'

# iterable
Gender_CHOICES =(
    ("male", "male"),
    ("female", "female"),
    ("not specified", 'not specified'),
    
)
Class_CHOICES =(
    ("1st", "1st"),
    ("2st", "2st"),
    ("3st", '3st'),
    ("4st", '4st'),
    ("5st", '5st'),
    ("6st", '6st'),
    ("7st", '7st'),
    ("8st", '8st'),
    ("9st", '9st'),
    ("10st", '10st'),
    ("11st", '11st'),
    ("12st", '12st'),
    
)
Subject_CHOICES =(
    ("Hindi", "Hindi"),
    ("English", "English"),
    ("Math", "Math"),
    ("Social science", "Social science"),
    ("Science", "Science"),
    ("biology", "biology"),
    ("chemistry", "chemistry"),
    ("physics", "physics"),
    ("Mathematics", "Mathematics"),
    ("I.T (Information Technology)", "I.T (Information Technology)"),
    ("Accountancy", "Accountancy "),
    ("Business Studies(B.O)", "Business Studies(B.O)"),
    ("Economics", "Economics"),
    ("History", "History"),
    ("Political Science", "Political Science"),
    ("Geography", "Geography"),
    ("Sociology", "Sociology"),
   
    
)
class StudentRegistrationAdmin(forms.ModelForm):
    gender = forms.ChoiceField(choices = Gender_CHOICES)
    stud_class = forms.ChoiceField(choices = Class_CHOICES)
    subject_name = forms.MultipleChoiceField(choices = Subject_CHOICES)
    # Phone_no = forms.CharField(max_length=10, validators=[RegexValidator(
    #     '^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$', message="Enter a Valid Indian Phone Number")])
 
    class Meta:
        model = StudentProfile
        fields = "__all__"
        # fields = ['id', 'name', 'dob', 'Roll_no', 'stud_class', 'Phone_no', 'subject_name', 'attendance_date', 'gender', 'fees', 'address']
        widgets = {'only_user_name' : forms.TextInput(attrs={'class':'form-control'}),
        'name' : forms.TextInput(attrs={'class':'form-control'}),
        'dob' : HTML5DateWidget(),
        'Roll_no' : forms.NumberInput(attrs={'class':'form-control'}),
        'stud_class' : forms.NumberInput(attrs={'class':'form-control'}),
        'father_name' : forms.TextInput(attrs={'class':'form-control'}),
        'mother_name' : forms.TextInput(attrs={'class':'form-control'}),
        'Phone_no' : forms.NumberInput(attrs={'class':'form-control'}),
        'subject_name' : forms.TextInput(attrs={'class':'form-control'}),
        'gender' : forms.TextInput(attrs={'class':'form-control'}),
        'fees' : forms.NumberInput(attrs={'class':'form-control'}),
        'attendance_date' : HTML5DateWidget(),
        'address' : forms.TextInput(attrs={'class':'form-control'}),}

class TeacherRegistrationAdmin(forms.ModelForm):
    gender = forms.ChoiceField(choices = Gender_CHOICES)
    stud_class = forms.ChoiceField(choices = Class_CHOICES)
    subject_name = forms.ChoiceField(choices = Subject_CHOICES)
    class Meta:
        model = Teacher
        fields = "__all__"
        # fields = ['id', 'name', 'dob', 'stud_class', 'Phone_no', 'subject_name', 'attendance_date', 'gender', 'salary', 'address']
        widgets = {'only_user_name' : forms.TextInput(attrs={'class':'form-control'}),
        'name' : forms.TextInput(attrs={'class':'form-control'}),
        'dob' : HTML5DateWidget(),
        'date' : HTML5DateWidget(),
        'father_name' : forms.TextInput(attrs={'class':'form-control'}),
        'mother_name' : forms.TextInput(attrs={'class':'form-control'}),
        'stud_class' : forms.NumberInput(attrs={'class':'form-control'}),
        'Phone_no' : forms.NumberInput(attrs={'class':'form-control'}),
        'subject_name' : forms.TextInput(attrs={'class':'form-control'}),
        'gender' : forms.TextInput(attrs={'class':'form-control'}),
        'salary' : forms.NumberInput(attrs={'class':'form-control'}),
        'attendance_date' : HTML5DateWidget(),
        'address' : forms.TextInput(attrs={'class':'form-control'}),}


    

class ContractorRegistrationAdmin(forms.ModelForm):
    gender = forms.ChoiceField(choices = Gender_CHOICES)
    class Meta:
        model = Contractor
        fields = "__all__"
        # fields = ['id', 'name', 'dob', 'Phone_no', 'attendance_date', 'gender', 'payment', 'address']
        widgets = {'only_user_name' : forms.TextInput(attrs={'class':'form-control'}),
        'name' : forms.TextInput(attrs={'class':'form-control'}),
        'dob' : HTML5DateWidget(),
        'date' : HTML5DateWidget(),
        'Phone_no' : forms.NumberInput(attrs={'class':'form-control'}),
        'father_name' : forms.TextInput(attrs={'class':'form-control'}),
        'mother_name' : forms.TextInput(attrs={'class':'form-control'}),
        'payment' : forms.NumberInput(attrs={'class':'form-control'}),
        'attendance_date' : HTML5DateWidget(),
        'address' : forms.TextInput(attrs={'class':'form-control'}),}

class StudentMarksheetForm(forms.ModelForm):
    class Meta:
        model = StudentMarksheet
        fields = "__all__"
        # fields = ['id', 'sm_stud_roll', 'sm_name', 'sm_dob', 'sm_date','sm_father_name', 'sm_mother_name','subject_1','subject_2','subject_3','subject_4','subject_5','subject_6']
        widgets = {'sm_stud_roll' : forms.NumberInput(attrs={'class':'form-control'}),
        'sm_name' : forms.TextInput(attrs={'class':'form-control'}),
        'sm_dob' : HTML5DateWidget(),
        'sm_date' : HTML5DateWidget(),
        'sm_father_name' : forms.TextInput(attrs={'class':'form-control'}),
        'sm_mother_name' : forms.TextInput(attrs={'class':'form-control'}),
        'subject_1' : forms.NumberInput(attrs={'class':'form-control'}),
        'subject_2' : forms.NumberInput(attrs={'class':'form-control'}),
        'subject_3' : forms.NumberInput(attrs={'class':'form-control'}),
        'subject_4' : forms.NumberInput(attrs={'class':'form-control'}),
        'subject_5' : forms.NumberInput(attrs={'class':'form-control'}),
        'subject_6' : forms.NumberInput(attrs={'class':'form-control'})
        }