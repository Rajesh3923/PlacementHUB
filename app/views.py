from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Studentnew, AdminRegistration,Company,StudentQueries,AppliedStudents
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
# import openpyxl




#----------- view for retriving the student details for admin dashboard-----------------

def student_admin(request):
    students = Studentnew.objects.all()
    no_of_students=Studentnew.objects.count()
    applied=AppliedStudents.objects.all()
    context={'students': students,'no_of_students':no_of_students,'applied':applied}
    return render (request,'student_admin.html',context )


#-----------------------------------------------------------------------------

# ---------------view for retriving the admin details for admin profile-----------------

def admin_profile(request):
    user=request.user
    current_user=user.username
    data=AdminRegistration.objects.get(admin_id=current_user)
    context={'datas':data}
    return render(request,'admin_profile.html',context)

#-----------------------------------------------------------------------------


#---------------------Admin login----------------------------------------------
def adminlogin(request):
    if request.method=="POST":
        userid=request.POST.get('userid')
        password=request.POST.get('password')

        user=auth.authenticate(request,username=userid,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('student_admin')
        else:
            error_message = 'Invalid credentials'
            return render(request, 'adminlogin.html', {'error_message': error_message})
    else:  
        return render(request, 'adminlogin.html')

#--------------------------------------------------------------------
#---------------student login----------------------------------------
def studentlogin(request):
    if request.method == 'POST':
        userid = request.POST['userid']  # Assuming 'userid' is the email
        password = request.POST['password']  # Assuming 'password' is the registration number

        # Authenticate the user based on email and registration number
        user=auth.authenticate(username=userid,password=password)

        if user is not None:
            # User is authenticated, log them in
            auth.login(request,user)
            return redirect('student_dashboard')  # Redirect to the student dashboard
        else:
            error_message = 'Invalid credentials'
            return render(request, 'studentlogin.html', {'error_message': error_message})

    return render(request, 'studentlogin.html')

#-------------------------------------------------------------------------
#-----------------student_dashboard for profile page---------------------------------------
def student_dashboard(request):
    student1=Studentnew.objects.all()
    context={'userid':student1}
    return render (request,"student_dashboard.html",context)
#-------------------------------------------------------------------

#-----------------student_dashboard for matching companies---------------------------------------


def upload_resume(request):
    if request.method == 'POST':
        # Get the uploaded resume file
        resume_file = request.FILES.get('resume')

        # Ensure the user is logged in
        if request.user.is_authenticated:
            # Get the current user
            current_user = request.user.username

            # Get or create the Studentnew model for the current user
            student, created = Studentnew.objects.get_or_create(registrationNumber=current_user)

            # Update the resume field with the uploaded resume
            student.resume = resume_file
            student.save()

    return redirect('student_dashboard')


#--------------------------applied resumes---------
def applied_upload_resume(request):
    if request.method == 'POST':
        resume = request.FILES['resume']
        company_name = request.POST.get('company_name')
        # print("hi"+company_name)
        user = request.user
        applied_student = AppliedStudents(student=user.username,name=company_name,resume=resume)
        applied_student.save()
        return redirect('match')
    return redirect('student_dashboard')
#--------------------------------------------------------------


#------------------fetching matching into page -----------------


#----------------------REGISTRATION FORM--------------------


def stureg(request):
    if request.method == 'POST':
        registrationNumber = request.POST.get('registrationNumber')
        
        # Check if the registration number already exists in the database
        if Studentnew.objects.filter(registrationNumber=registrationNumber).exists():
            # Registration number already taken, display error message
            error_message = 'Registration number already taken 🚫'
            return render(request, 'stureg.html', {'error_message': error_message})

        # Process the registration form data
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        degree = request.POST.get('degree')
        gpa12 = request.POST.get('gpa12')
        gpaBtech = request.POST.get('gpaBtech')
        backlogs = request.POST.get('backlogs')
        project_url = request.POST.get('projectUrl')
        skills = request.POST.getlist('skills[]')
        languages = request.POST.get('languages')

        user=User.objects.create_user(username=registrationNumber, password=dob)
        user.save()
        # Create a new Student object and save it to the database
        student = Studentnew.objects.create(
            registrationNumber=registrationNumber,
            name=name,
            dob=dob,
            gender=gender,
            phone=phone,
            email=email,
            degree=degree,
            gpa12=gpa12,
            gpaBtech=gpaBtech,
            backlogs=backlogs,
            project_url=project_url,
            skills=','.join(skills),
            languages=languages,
            
        )
        subject = 'Welcome to Our Website'
        context = {'name': name}  
        html_message = render_to_string('success.html', context)
        plain_message = strip_tags(html_message)  # Convert HTML to plain text
        from_email = '21a81a0539@gmail.com'  # Set the sender's email address
        recipient_list = [student.email]  # Set the recipient's email address
        send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

        return render(request,'success.html',{'name':name })

    return render(request, 'stureg.html')





















#-----------------------------------STUDENT LOGIN------------------------
@login_required
def student_profile(request):
    current_user=request.user
    userid=current_user.username
    profile=Studentnew.objects.get(registrationNumber=userid)  
    context={
        
        'profile':profile
    }
    return render(request, 'student_profile.html', context)

#-----------------------------------------admin registration-----------------
#--------------------matching companies-------------------
@login_required
def match(request):
    # Get the current user and student profile
    current_user = request.user
    userid = current_user.username
    student_profile = Studentnew.objects.get(registrationNumber=userid)
    student_skills = student_profile.skills.split(",")  # Assuming skills are comma-separated in the model
    # print(student_skills)
    # print(type(student_skills))
    matching_companies = []
    for skill in student_skills:
         matching_companies.extend(Company.objects.filter(skills_required__contains=skill))
    context = {
        'matching_companies': matching_companies,
    }
    return render(request, 'match.html', context)

#------------------------------------------------------------------------------------------


def register_admin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        full_name = request.POST.get('full_name')
        admin_id = request.POST.get('admin_id')
        feedback = request.POST.get('feedback')  # Retrieve the "feedback" field from the POST data

        experience = request.POST.get('experience')

        user=User.objects.create_user(username=admin_id,password=password)
        user.save()

        # Create a new AdminRegistration object and save it to the database
        admin = AdminRegistration.objects.create(
            email=email,
            password=password,
            confirm_password=confirm_password,
            full_name=full_name,
            admin_id=admin_id,
            feedback=feedback,
            experience=experience
        )
        subject = 'Welcome to Our Website'
        context = {'name': full_name}  
        html_message = render_to_string('successadmin.html', context)
        plain_message = strip_tags(html_message)  # Convert HTML to plain text
        from_email = '21a81a0539@gmail.com'  # Set the sender's email address
        recipient_list = [admin.email]  # Set the recipient's email address
        send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

        return redirect('successadmin')
    
    return render(request, 'register_admin.html')

#------------------------------------------companies view function --------------------------------------
def admin_add_company(request):
    if request.method == 'POST':
        logo = request.FILES['logo']
        name = request.POST['name']
        job_role = request.POST['job_role']
        salary_package = request.POST['salary_package']
        skills_required = request.POST['skills_required']
        

        Company.objects.create(
            logo=logo,
            name=name,
            job_role=job_role,
            salary_package=salary_package,
            skills_required=skills_required
        )
        return redirect('student_admin')
    return render(request, 'studentlogin.html')
#--------------------------------------------------------------------------
def student_dashboard(request):
    companies = Company.objects.all()
    # user=request.user
    # curr_user=user.username
    # appliedCompanies=AppliedStudents.objects.filter(student=curr_user)
    # print("hi"+appliedCompanies)
    return render(request, 'student_dashboard.html', {'companies': companies})
#----------------------------------------------------
#----------------------Applied companies by studnet----------
def retrived(request):
    userid=request.user
    curr_user=userid.username
    # print(curr_user)
    appliedCompanies=AppliedStudents.objects.filter(student=curr_user)
    # print("hi",appliedCompanies)
    return render(request,'student_dashboard.html',{'appliedCompanies':appliedCompanies})


#--------------------------Student contact form-------------------------------------------
@csrf_protect
def student_dashboardQuery(request):
    if request.method == 'POST':
        email = request.POST['email']
        query = request.POST['Query']
        mobile = request.POST['mobile']
        # Use the create method to save the data to the model
        StudentQueries.objects.create(email=email, query=query,mobile=mobile)
        messages.success(request, 'Query submitted successfully.')
        # Redirect or return a response as needed
        return render(request,'student_dashboard.html')  # Redirect to a success page

    return render(request, 'success.html')



#--------------------------studentqueryiinto admin page-----------
def student_adminissues(request):
    student_queries = StudentQueries.objects.all().order_by('-arrival_time')
    # print(student_queries)
    # Pass the data to the "student_admin" template
    context = {'issues': student_queries}
    return render(request, 'student_adminissues.html', context)


#----------------------- landing main--------------------------------------------------
def landing (request):
    return render(request,'landing.html')




#-----------logout----------------
def logout_user(request):
    logout(request)  # Log out the current user
    return redirect('studentlogin')









def success(request):
   #currentuser
    userid = "Mr"  # Replace with your logic to retrieve the user ID
    return render(request, 'success.html', {'userid': userid})
    return redirect('studentlogin')

def successadmin(request):
    
    userid = "welcome"  # Replace with your logic to retrieve the user ID
    return render(request, 'successadmin.html', {'userid': userid})
    return redirect('adminlogin')

