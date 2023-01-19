from django.forms import ModelForm, EmailField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    # def save(self, commit=True):
    #     data = self.cleaned_data
    #     user = User(username=data['username'], email=data['email'], password1=data['password1'],
    #                 password2=data['password2'])
    #     user.save()
    #     return user

class UpdateUserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
