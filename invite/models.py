from django.db import models

from django.db import models

class GuestResponse(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    attending = models.BooleanField()

    def __str__(self):
        return self.name