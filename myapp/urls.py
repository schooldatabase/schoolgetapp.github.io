from django.urls import path
from myapp import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('studnetdownload/', views.studnet_download, name='studnetdownload'),
    path('studrolldob/', views.stud_roll_dob, name='studrolldob'),
    path('student/', views.student_show, name='student'),
    path('studentmarksheet/', views.student_mark_sheet, name='studentmarksheet'),
    path('studenttable/', views.student_mark_sheet_table, name='studenttable'),
    path('teacher/', views.teacher_show, name='teacher'),
    path('contractor/', views.contractor_show, name='contractor'),
    path('studentupdatedata/<int:id>/', views.student_update_data, name='studentupdatedata'),
    path('studentdeletedata/<int:id>/', views.student_delete_data, name='studentdeletedata'),
    path('teacherupdatedata/<int:id>/', views.teacher_update_data, name='teacherupdatedata'),
    path('teacherdeletedata/<int:id>/', views.teacher_delete_data, name='teacherdeletedata'),
    path('contractorupdatedata/<int:id>/', views.contractor_update_data, name='contractorupdatedata'),
    path('contractordeletedata/<int:id>/', views.contractor_delete_data, name='contractordeletedata'),
    path('register/', views.register_attempt, name='register_attempt'),
    path('login/', views.login_attempt, name='login_attempt'),
    path('logout/', views.logout_view, name='logout'),
    path('verify/<auth_token>/', views.verify, name='verify'),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)