from django.urls import path
from . import views

urlpatterns = [
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('student_dashboard/',views.student_dashboard,name='student_dashboard'),
    path('studentlogin/student_dashboard/',views.student_dashboard,name='student_dashboard'),
    path('studentlogin/stureg/', views.stureg, name='stureg'),
    path('success/', views.success, name='success'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminlogin/register_admin/',views.register_admin,name='register_admin'),
    path('student_admin/',views.student_admin,name='student_admin'),
    path('successadmin/', views.successadmin, name='successadmin'),
    path('student_admin/admin_profile',views.admin_profile,name='admin_profile'),
    path('student_admin/adminlogin/',views.adminlogin,name='adminlogin'),
    path('student_profile/',views.student_profile,name='student_profile'),
    path('register_admin/',views.register_admin,name='register_admin'),
    path('upload_resume/', views.upload_resume, name='upload_resume'),





]