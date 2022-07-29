from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Registrationform(UserCreationForm):
    class Meta:
        model = User
        field = ("username", "email")