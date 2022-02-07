"""BaseApp views"""

from django.views.generic import ListView
from .models import Message


class GuestbookView(ListView):
    """Guestbook main view"""

    model = Message
    template_name = "base/guestbook.html"
    context_object_name = "messages"
