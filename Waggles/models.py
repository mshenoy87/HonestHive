from django.db import models

# Create your models here.
class Waggle(models.Model):
    # id - Primary key
    waggleText = models.TextField(blank=True, null=True)
    waggleImage = models.FileField(upload_to="images/", blank=True, null=True)
    