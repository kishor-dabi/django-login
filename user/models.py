from django.db import models

# Create your models here.
# from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def set_password(self, raw_password):
        self.password = raw_password
