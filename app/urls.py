from django.urls import path
from . import views

urlpatterns = [
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('student_dashboard/',views.student_dashboard,name='student_dashboard'),
    path('match/',views.match,name='match'),
    path('student_dashboard/',views.student_dashboardQuery,name='student_dashboard'),

    path('student_dashboardQuery/', views.student_dashboardQuery, name='student_dashboardQuery'),

    path('studentlogin/student_dashboard/',views.student_dashboard,name='student_dashboard'),
    path('studentlogin/stureg/', views.stureg, name='stureg'),
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('applied_upload_resume/', views.applied_upload_resume, name='applied_upload_resume'),
    path('success/', views.success, name='success'),
    path('student_dashboard/', views.retrived, name='student_dashboard'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminlogin/register_admin/',views.register_admin,name='register_admin'),
    path('student_admin/',views.student_admin,name='student_admin'),
    path('successadmin/', views.successadmin, name='successadmin'),
    path('student_admin/admin_profile',views.admin_profile,name='admin_profile'),
    path('student_adminissues/', views.student_adminissues, name='student_adminissues'),
    path('student_admin/adminlogin/',views.adminlogin,name='adminlogin'),
    path('student_profile/',views.student_profile,name='student_profile'),
    path('register_admin/',views.register_admin,name='register_admin'),
    path('upload_resume/', views.upload_resume, name='upload_resume'),
    path('admin_add_company/',views.admin_add_company,name='admin_add_company'),
    path('landing/',views.landing,name='landing'),
    path('studentlogin/', views.logout_user, name='studentlogin'),








]