from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import  settings
from app.views import studentlogin,stureg,success,student_admin,register_admin,successadmin,admin_profile,adminlogin,student_dashboard,student_profile,admin_add_company,student_dashboardQuery,student_adminissues,match,landing,applied_upload_resume,retrived,logout_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing, name='landing'),
    path('studentlogin/', studentlogin, name='studentlogin'),
    path('studentlogin/stureg/',stureg, name='stureg'),
    path('applied_upload_resume/',applied_upload_resume, name='applied_upload_resume'),
    path('success/',success, name='success'),
    path('student_dashboard/',retrived, name='student_dashboard'),

    path('successadmin/',successadmin, name='successadmin'),
    path('app/', include('app.urls')),
    # path('student/', include('app.urls')),
    path('adminlogin/register_admin/',register_admin,name="register_admin"),
    path('student_admin/adminlogin/',adminlogin,name='adminlogin'),
    path('student_admin/',student_admin,name='student_admin'),
    path('student_adminissues/',student_adminissues,name='student_adminisues'),
    path('student_admin/admin_profile/',admin_profile,name='admin_profile'),
    path('adminlogin/',adminlogin,name='adminlogin'),
    # path('/',studentlogin,name='studentlogin'),
    path('match/',match,name='match'),
    path('studentlogin/student_dashboard',student_dashboard, name='student_dashboard'),
    path('student_dashboard',student_dashboard, name='student_dashboard'),
    path('student_dashboard/',student_dashboardQuery,name='student_dashboard'),

    path('student_dashboardQuery/',student_dashboardQuery, name='student_dashboardQuery'),

    path('student_profile',student_profile,name='student_profile'),
    path('register_admin/',register_admin,name='register_admin'),
    path('admin_add_company/',admin_add_company,name='admin_add_company'),
    path('logout_user/',logout_user, name='logout_user'),





    
    


]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
