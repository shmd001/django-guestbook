"""BaseApp URL Configuration"""

from django.urls import path
from .views import GuestbookView, UserSignin

urlpatterns = [
    path("", GuestbookView.as_view(), name="guestbook"),
    path("signin/", UserSignin.as_view(), name="signin"),
]
