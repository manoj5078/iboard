from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


app_name = 'Users'

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserForm(UserCreationForm):  
    class Meta:  
        model = User 
        fields = ['username','email', 'password1','password2'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'}), 
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
      }

class AdminloginForm(forms.Form):
    class Meta:
        model = User
        fields = ['username','password1']
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'}), 
            'password1':forms.PasswordInput(attrs={'class':'form-control'})
        }