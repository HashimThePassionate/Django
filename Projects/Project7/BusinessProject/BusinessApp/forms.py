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
class contactform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={"required": "Please enter your name"})

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),error_messages={"required": "Please enter password"} )

    matchpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),error_messages={"required": "Please enter password"},label="Password (again)" )
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')
        matchpassword =  cleaned_data.get('matchpassword')

        if password != matchpassword:
            self.add_error('password', 'Password does not match')
            self.add_error('matchpassword', 'Password does not match')

        if name and len(name) < 4:
            self.add_error('name', 'Name should not be less than 4')
        if password and 'password' in password.lower():
            self.add_error('password', 'Password should not contain the word "password"')

    # username=forms.CharField(widget=forms.TextInput(attrs={'class':'example1','id':'exampleid'}), required=True)
    # username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'exampleid'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'exampleid'}))
>>>>>>> f70a6a7f5382a5a39c22d5f759bbee8cada889d1
