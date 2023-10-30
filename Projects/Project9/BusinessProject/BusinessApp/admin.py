from django.contrib import admin
<<<<<<< HEAD
from .models import student
@admin.register(student)
class adminStudent(admin.ModelAdmin):
    list_display=('id','student_name','student_email','student_course','student_progress')
    
=======
from .models import user
@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display=('id','name','password')

>>>>>>> f70a6a7f5382a5a39c22d5f759bbee8cada889d1
