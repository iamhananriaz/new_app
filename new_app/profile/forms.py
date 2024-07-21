from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address', 'profile_photo']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must be numeric")
        return phone_number