from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
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
        
class customregistration(UserCreationForm):
    password1=forms.CharField(min_length=8, max_length=60,widget=forms.PasswordInput(attrs={'class':'form-control','id':'password1'}),label="Password")
    password2=forms.CharField(min_length=8, max_length=60,widget=forms.PasswordInput(attrs={'class':'form-control','id':'password2'}),label="Confirm Password") 

    class Meta:
        model = User
        fields = ['username','email']
        widgets= {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            # 'first_name':forms.TextInput(attrs={'class':'form-control'}),
            # 'last_name':forms.TextInput(attrs={'class':'form-control'}),
        }


class userEditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'username':'Name','email':'Email'}