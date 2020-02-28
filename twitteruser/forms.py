from django import forms
from twitteruser.models import TwitterUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

    class Meta:
        model = TwitterUser
        fields = ['username', 'password']
