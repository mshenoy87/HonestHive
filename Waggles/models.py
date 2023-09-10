from django.db import models
from random import randint

##################################
# When changing the model run these commands in this order:
    # ./manage.py makemigrations
    # ./manage.py migrate
##################################

# Create your models here.
class Waggle(models.Model):
    # id - Primary key
    waggleText = models.TextField(blank=True, null=True)
    waggleImage = models.FileField(upload_to="images/", blank=True, null=True)

    # reverse the ordering (first waggle is bottom of screen)
    class Meta:
        ordering = ['-id']

    def serialize(self):
        # return a dictionary of the model
        return {
            "id": self.id,
            "waggleText": self.waggleText,
            "likes": randint(0, 10)
        }
    