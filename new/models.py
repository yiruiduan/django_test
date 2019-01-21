from django.db import models

# Create your models here.
class NewUserInfo(models.Model):
    user_name=models.CharField(max_length=32)
    user_pwd=models.CharField(max_length=20)
    user_tel=models.CharField(max_length=20)
    user_email=models.CharField(max_length=32)