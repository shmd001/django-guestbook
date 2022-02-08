"""BaseApp models"""

from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """Message model"""

    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # May be IP?

    class Meta:
        """Meta class for ordering messages from new to old"""

        ordering = ["-created_at"]
