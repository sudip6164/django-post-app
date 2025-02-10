from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    # Optionally add custom help_text
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        help_text="Your password must contain at least 8 characters, "
                  "and can't be a commonly used password or entirely numeric."
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        help_text="Enter the same password as before for verification."
    )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'bio-input'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'profile-picture-input'}),
        }