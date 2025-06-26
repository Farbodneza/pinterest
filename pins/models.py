from django.db import models
from taggit.managers import TaggableManager
# Upload Pin (Image, title, description, tags)
# Create your models here.
class Pin(models.Model):
    image = models.ImageField(upload_to = "media/images")
    title = models.CharField(max_length=150)
    description = models.TextField()
    tags = TaggableManager()


class Wishlist(models.Model):

# Wishlist (Save pins to a "Saved for Later" list)