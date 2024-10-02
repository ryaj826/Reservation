from django.db import models

# Create your models here.
from django.db import models

class Reservation(models.Model):
    user = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.user} - {self.room} ({self.check_in} to {self.check_out})'
