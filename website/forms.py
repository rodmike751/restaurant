from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model 
from django import forms
User = get_user_model()


class EditUserForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "autocomplete": "off",
                "style":"width:100%",
                "placeholder":"Last name",
                "required": False,
            }
        ),
    )
    last_name = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "autocomplete": "off",
                "style":"width:100%",
                "placeholder":"Last name",
                "required": False,
            }
        ),
    )
    username = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "autocomplete": "off",
                "style":"width:100%",
                "placeholder":"Last name",
                "required": True,
            }
        ),
    )
    email = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "autocomplete": "on",
                "style":"width:100%",
                "placeholder":"Email",
                "required": True,
            }
        ),
    )
   
    class Meta:
        model = User 
        fields = ["first_name", "last_name", "username", "email"]


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "autocomplete": "on",
                "placeholder":"First name",
                "required": True,
            }
        ),
    )
    last_name = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "autocomplete": "off",
                "placeholder":"Last name",
                "required": True,
            }
        ),
    )
    username = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "autocomplete": "off",
                "placeholder":"Last name",
                "required": True,
            }
        ),
    )
    email = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "autocomplete": "on",
                "placeholder":"Email",
                "required": True,
            }
        ),
    )
    password1 = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "autocomplete": "off",
                "placeholder":"Password",
                "required": True,
            }
        ),
    )
    password2 = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "autocomplete": "off",
                "placeholder":"Confirm password",
                "required": True,
            }
        ),
    )
    class Meta:
        model = User 
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "autocomplete": "on",
                "placeholder":"Username",
                "required": True,
            }
        ),
    )
    password = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "autocomplete": "off",
                "placeholder":"Password",
                "required": True,
            }
        ),
    )