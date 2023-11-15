from django.contrib import admin
from .models import Student, Library
@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display=('id','student_name','student_email','student_course','student_progress')
@admin.register(Library)
class libraryAdmin(admin.ModelAdmin):
    list_display=('librarian','books','library_card','wifi')