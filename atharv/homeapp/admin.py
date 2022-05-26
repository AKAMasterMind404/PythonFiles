from django.contrib import admin

# Register your models here.
from .models import UserModelCustom

admin.site.register(UserModelCustom)
