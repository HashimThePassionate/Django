from django import forms
from Blog.models import Blog
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class contact(forms.Form):
    name = forms.CharField(max_length=50,error_messages={'required':'Please Enter Your Name'},widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Name'}))
    email = forms.EmailField(max_length=254,error_messages={'required':'Please Enter Your Email'},widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email'}))
    phoneno = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'PhoneNo'}),required=False)
    message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Message'}),required=False)


class sigupContactForm(UserCreationForm):
    password1=forms.CharField(min_length=8, max_length=60,widget=forms.PasswordInput(attrs={'class':'form-control','id':'password1','placeholder': 'Password'}),label="Password")
    password2=forms.CharField(min_length=8, max_length=60,widget=forms.PasswordInput(attrs={'class':'form-control','id':'password2','placeholder': 'Confirm Password'}),label="Confirm Password") 

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        widgets= {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder': 'Username'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Last Name'}),
        }


class signin(AuthenticationForm):
    username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'}))



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','des']
        labels = {'title':'Title','des':'Description'}
        widgets= {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'des':forms.Textarea(attrs={'placeholder':'Description','class':'form-control'})
        }