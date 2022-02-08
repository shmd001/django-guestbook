"""BaseApp forms"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from base.models import Message


class SendMessageForm(forms.ModelForm):
    """Send messge form"""

    text = forms.CharField(
        max_length=255,
        min_length=1,
        label="Message",
        label_suffix="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "floatingTextarea",
            }
        ),
    )

    class Meta:
        """Meta class for ModelForm"""

        model = Message
        fields = ["text"]


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


class SignupForm(UserCreationForm):
    """Custom signup form"""

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

    password1 = forms.CharField(
        max_length=60,
        min_length=6,
        label="Password",
        label_suffix="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control rounded-4",
                "id": "floatingPassword1",
            }
        ),
    )

    password2 = forms.CharField(
        max_length=60,
        min_length=6,
        label="Password confirmation",
        label_suffix="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control rounded-4",
                "id": "floatingPassword2",
            }
        ),
    )
