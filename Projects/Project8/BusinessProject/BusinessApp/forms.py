from django import forms
from .models import Student
class contact(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name','student_email','student_course']
        labels = {'student_name':'Name','student_email':'Email','student_course':'Course'}
        error_messages = {'student_name':{'required':'Please Enter Your Valid Name'},
        'student_email':{'required':'Please Enter Your email with @'},
        'student_course':{'required':'Please Enter Your Course Name'}
        }
        widgets= {
            'student_name':forms.TextInput(attrs={'placeholder':'Enter Your Name'}),
            'student_email':forms.EmailInput(attrs={'placeholder':'example@gmail.com'})
        }