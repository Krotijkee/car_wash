from django.db import models
from django.core.validators import EmailValidator
from django.utils.timezone import now

# Create your models here.

class Review(models.Model):
    default_validators = [EmailValidator]
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(default=now)
    name = models.CharField(max_length=30)
    text = models.TextField(blank=False)
    email = models.CharField(max_length=30, default="none@mail.com")

    def __str__(self):
        return str(self.id) + "_" + str(self.name) + "_" + str(self.email) + "_" + str(self.date) + "_" + str(self.text)