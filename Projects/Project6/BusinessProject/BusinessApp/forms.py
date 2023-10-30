from django import forms
<<<<<<< HEAD
from .models import student
from django.forms import ModelForm
class studentForm(ModelForm):
    # name = forms.CharField(widget=)
    class Meta:
        student_name = forms.CharField(required=False)
        model = student
        fields = ['student_name','student_email','student_course']
        labels = {'student_name':'Name',
                'student_email':'Email',
                'student_course':'Subject'}
        error_messages = {
            'student_name': {
                'required':'Please Enter Your Name'
            },
             'student_email': {
                'required':'Please Enter Your Email'
            },
            
        }
        widgets = { 'student_email':forms.EmailInput(attrs={'placeholder':'example@gmail.com'})}
=======
class studentRegistration(forms.Form):
    name=forms.CharField(label="Enter Your Name", label_suffix="",disabled=True)
    email=forms.EmailField(help_text="Enter email with @")
>>>>>>> f70a6a7f5382a5a39c22d5f759bbee8cada889d1
