from django import forms
from .models import User
# from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, PasswordInput


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        # fields = ('first_name', 'last_name', 'username', 'email', 'password')
        fields = ('name', 'email', 'password')

        widgets = {
            'password': PasswordInput(),
        }
        # fields = "__all__"


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'password': PasswordInput(),
        }
