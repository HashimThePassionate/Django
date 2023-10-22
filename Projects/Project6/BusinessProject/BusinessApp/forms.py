from django import forms
class studentRegistration(forms.Form):
    name=forms.CharField(label="Enter Your Name", label_suffix="",disabled=True)
    email=forms.EmailField(help_text="Enter email with @")
