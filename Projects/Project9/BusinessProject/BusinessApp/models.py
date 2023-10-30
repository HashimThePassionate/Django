from django.db import models
<<<<<<< HEAD
class student(models.Model):
    student_name=models.CharField(max_length=50)
    student_email=models.EmailField(max_length=254)
    student_course=models.CharField(max_length=50)
    student_progress=models.TextField()
=======
class user(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
>>>>>>> f70a6a7f5382a5a39c22d5f759bbee8cada889d1
