from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignupForm(UserCreationForm):
    age = forms.IntegerField(required=True, label="나이")
    job = forms.CharField(max_length=10, label="직업")
    mbti = forms.CharField(max_length=30, label="MBTI")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'job', 'age', 'mbti']
