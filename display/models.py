from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50, blank=False, verbose_name="Name")
    phone = models.CharField(max_length=20, blank=False, verbose_name="Phone Number")
    email = models.CharField(max_length=50, blank=False, verbose_name="Email")

    def __str__(self):
        return self.name
