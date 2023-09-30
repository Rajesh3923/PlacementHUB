from django.contrib.auth.backends import ModelBackend
from .models import Studentnew

class StudentBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            student = Studentnew.objects.get(email=username)
        except Studentnew.DoesNotExist:
            return None
        
        if student.registrationNumber == password:
            return student
        
        return None
