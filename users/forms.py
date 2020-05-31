from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #default the email is required information

    class Meta:
        # 
        model = User # This is the model that we want this form interact with, because new user is generated.
        fields = ['username', 'email', 'password1', 'password2']