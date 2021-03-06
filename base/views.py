"""BaseApp views"""

from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message
from .forms import SigninForm, SignupForm, SendMessageForm


class GuestbookView(LoginRequiredMixin, ListView, FormView):
    """Guestbook main view"""

    model = Message
    form_class = SendMessageForm
    success_url = reverse_lazy("guestbook")
    template_name = "base/guestbook.html"
    context_object_name = "messages"

    def form_valid(self, form):

        message = form.save(commit=False)
        message.user = self.request.user
        message.save()

        return super().form_valid(form)


class EditMessage(LoginRequiredMixin, UpdateView):
    """Message edit view"""

    model = Message
    template_name = "base/edit_message.html"
    success_url = reverse_lazy("guestbook")
    fields = ["text"]

    def get(self, request, *args, **kwargs):

        # Check if the message belongs to user
        if request.user != Message.objects.get(id=kwargs["pk"]).user:
            return HttpResponseRedirect(reverse_lazy("guestbook"))

        return super().get(request, *args, **kwargs)


class DeleteMessage(LoginRequiredMixin, DeleteView):
    """Message delete view"""

    model = Message
    template_name = "base/delete_message.html"
    success_url = reverse_lazy("guestbook")

    def get(self, request, *args, **kwargs):

        # Check if the message belongs to user
        if request.user != Message.objects.get(id=kwargs["pk"]).user:
            return HttpResponseRedirect(reverse_lazy("guestbook"))

        return super().get(request, *args, **kwargs)


class UserSignin(LoginView):
    "Login view"

    template_name = "base/signin.html"
    form_class = SigninForm
    redirect_authenticated_user = True
    next_page = reverse_lazy("guestbook")


class UserSignout(LogoutView):
    """Logout view"""

    next_page = reverse_lazy("signin")


class UserSignup(FormView):
    """Register view"""

    form_class = SignupForm
    success_url = reverse_lazy("guestbook")
    template_name = "base/signup.html"

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("guestbook"))

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):

        user = form.save()

        if user is not None:
            login(self.request, user)

        return super().form_valid(form)
