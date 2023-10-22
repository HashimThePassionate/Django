from django import forms
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