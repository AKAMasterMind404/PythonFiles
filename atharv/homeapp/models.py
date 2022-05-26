from django.db import models

# Create your models here.
from django.db.models import *


class UserModelCustom(models.Model):
    name = CharField(max_length=30, null=True)
    age = IntegerField(default=18, null=True)
