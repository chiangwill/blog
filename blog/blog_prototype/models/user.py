from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_delete


class User(AbstractUser):

    class Meta:
        db_table = 'auth_user'

    def save(self, *args, **kwargs):
        self.clean()
        super(User, self).save(*args, **kwargs)
