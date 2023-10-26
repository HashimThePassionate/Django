from django.contrib import admin
from .models import student
@admin.register(student)
class adminStudent(admin.ModelAdmin):
    list_display=('id','student_name','student_email','student_course','student_progress')
    