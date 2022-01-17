from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegistrationform(UserCreationForm): #inheriting Usercreation form and add one extra
                                                 #email field
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']  #order of fields important here

