from django.contrib.auth.models import User
from django.db import models
from hashid_field import HashidField


class URL(models.Model):
    id = HashidField(primary_key=True)
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
