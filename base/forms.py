"""BaseApp forms"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm


class SigninForm(AuthenticationForm):
    """Custom signin form"""

    username = forms.CharField(
        max_length=60,
        min_length=3,
        label="Username",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded-4",
                "id": "floatingInput",
            }
        ),
    )

    password = forms.CharField(
        max_length=60,
        min_length=6,
        label="Password",
        label_suffix="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control rounded-4",
                "id": "floatingPassword",
            }
        ),
    )

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
