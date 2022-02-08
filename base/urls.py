"""BaseApp URL Configuration"""

from django.urls import path
from .views import GuestbookView, UserSignin, UserSignout, UserSignup, EditMessage

urlpatterns = [
    path("", GuestbookView.as_view(), name="guestbook"),
    path("signin/", UserSignin.as_view(), name="signin"),
    path("signout/", UserSignout.as_view(), name="signout"),
    path("signup/", UserSignup.as_view(), name="signup"),
    path("editmessage/<int:pk>/", EditMessage.as_view(), name="message-edit"),
]
