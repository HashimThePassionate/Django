from django import forms
class studentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
