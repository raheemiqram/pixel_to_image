from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthenticationMethod(models.TextChoices):
    EMAIL = "email", _("Email")
    USERNAME = "username", _("Username")
    USERNAME_EMAIL = "username_email", _("Username Email")
