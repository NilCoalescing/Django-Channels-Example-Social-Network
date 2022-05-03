from django.contrib.auth import get_user_model, logout, login
from django.http import HttpResponse


def login_view(request, username, **kwargs):
    """
    Do not consider this a a proper way to login a user!

    This is just to make the demo server simpler nothing more!
    """
    user, _ = get_user_model().objects.get_or_create(
        username=username,
    )

    login(request, user)

    return HttpResponse()


def logout_view(request):
    logout(request)
    return HttpResponse()
