from django import forms
from django.contrib.auth.models import User
 
 
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")
 
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
 
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
 
        if password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")
        return cleaned_data