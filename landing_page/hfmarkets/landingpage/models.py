from django.db import models
from django.contrib.auth.hashers import make_password

class TblUsers(models.Model):
    username = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.email} - {self.country} ({self.country_code}) - {self.phone}"
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(TblUsers, self).save(*args, **kwargs)
