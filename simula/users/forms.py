from django import forms
from .models import *

class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nom complet'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Mot de passe'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirmer mot de passe'}))

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Mot de passe'}))