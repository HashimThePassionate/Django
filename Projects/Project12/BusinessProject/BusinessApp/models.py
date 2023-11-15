from django.db import models
class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_email=models.EmailField(max_length=254)
    student_course=models.CharField(max_length=50)
    student_progress=models.TextField()

class Library(models.Model):
    librarian = models.CharField(max_length=50)
    books = models.CharField(max_length=50)
    library_card = models.CharField(max_length=50)
    wifi = models.BooleanField()