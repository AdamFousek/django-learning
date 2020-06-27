from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)
