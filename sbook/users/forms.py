from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'bio-input'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'profile-picture-input'}),
        }