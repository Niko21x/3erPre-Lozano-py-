from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):  # Cambia el nombre a ProfileForm
    class Meta:
        model = Profile
        fields = ['image', 'name', 'description', 'website']

from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']