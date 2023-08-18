from django.db import models
from random import randint
# Create your models here.
class Waggle(models.Model):
    # id - Primary key
    waggleText = models.TextField(blank=True, null=True)
    waggleImage = models.FileField(upload_to="images/", blank=True, null=True)

    def serialize(self):
        # return a dictionary of the model
        return {
            "id": self.id,
            "waggleText": self.waggleText,
            "likes": randint(0, 10)
        }
    