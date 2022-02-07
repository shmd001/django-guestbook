"""BaseApp views"""

from django.http import HttpResponse


def index(request):
    """Test"""

    return HttpResponse("Hello 👋🏻")
