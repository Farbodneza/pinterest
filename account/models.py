from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    profile = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.username