from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Replace the default User model with a custom one
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
