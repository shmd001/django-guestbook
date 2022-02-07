"""BaseApp views"""

from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Message
from .forms import SigninForm


class GuestbookView(ListView):
    """Guestbook main view"""

    model = Message
    template_name = "base/guestbook.html"
    context_object_name = "messages"


class UserSignin(LoginView):
    "Login view"

    template_name = "base/signin.html"
    form_class = SigninForm
    redirect_authenticated_user = True
    next_page = reverse_lazy("guestbook")


class UserSignout(LogoutView):
    """Logout view"""

    next_page = reverse_lazy("signin")
