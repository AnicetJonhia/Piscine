# myapp/models.py
from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date_time = models.DateTimeField()

    class Meta:
        db_table = 'users'

