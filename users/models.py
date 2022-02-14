import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True, name="id"
    )

    username = None
    email = models.EmailField("E-mail", unique=True)

    # verification data, to be sure the email is valid
    token_for_verification = models.CharField("Token de vérification", max_length=150)
    email_verified_date = models.DateTimeField("E-mail vérifie", blank=True, null=True)
    is_verified = models.BooleanField("E-mail valide", default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Utilisateurs"
