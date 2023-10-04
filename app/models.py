from django.db import models
from django.utils import timezone


class Studentnew(models.Model):
    registrationNumber = models.CharField(primary_key=True,max_length=10,default='')
    name = models.CharField(max_length=50)
    dob = models.IntegerField(null=True)
    gender = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    gpa12 = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    gpaBtech = models.DecimalField(max_digits=5, decimal_places=2)
    backlogs = models.CharField(max_length=50)
    degree = models.CharField(max_length=100, default='YourDefaultValueHere')
    project_url = models.URLField()
    skills = models.CharField(max_length=100, default='')
    languages = models.IntegerField(null=True)
    resume = models.FileField(upload_to='student_resumes/',default='')

    

    def __str__(self):
        return self.registrationNumber











class AdminRegistration(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    admin_id = models.CharField(max_length=50)
    feedback=models.CharField(max_length=150, default='')
    #area_of_expertise = models.ManyToManyField(ExpertiseArea)  # Many-to-many field for checkboxes
    experience = models.IntegerField()


    def __str__(self):
        return self.admin_id



#----------------------------companies data 
class Company(models.Model):
    logo = models.ImageField(upload_to='company_logos/')
    name = models.CharField(max_length=255)
    job_role = models.CharField(max_length=255)
    salary_package = models.DecimalField(max_digits=10, decimal_places=2)
    skills_required = models.TextField()

    def __str__(self):
        return self.name



#------------contact form-----------------
class StudentQuery(models.Model):
    email = models.EmailField()
    query = models.TextField() 
    arrival_time = models.DateTimeField(default=timezone.now)

    

    def __str__(self):
        return self.email