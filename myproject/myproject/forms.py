from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Name','bio','birth_date']



class CreateUserForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self,commit=True):
        user=super().save(comit=False)
        user.email= self.cleaned_data['email']
        if commit:
            user.save()
        return user
