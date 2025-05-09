from django import forms
from django.contrib.auth.models import User
from .models import Hire, Message, Hero


# ✅ Message Form
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Type your message...", "class": "form-control"})
        }


# ✅ Registration Form - NO SIGNALS
class RegistrationForm(forms.ModelForm):
    ROLE_CHOICES = (
        ("client", "Client"),
        ("hero", "Hero"),
        ("support", "Support"),
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password", "class": "form-control"})
    )
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]


# ✅ Hire Form
class HireForm(forms.ModelForm):
    class Meta:
        model = Hire
        fields = ["mission_name"]
        widgets = {
            "mission_name": forms.TextInput(attrs={
                "placeholder": "Enter mission name",
                "class": "form-control"
            }),
        }


# ✅ Profile Edit Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First name", "class": "form-control"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last name", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}),
        }


# ✅ Hero Update Form (with image support)
class HeroUpdateForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['description', 'price', 'power_level', 'available', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'power_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
