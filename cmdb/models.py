from django.db import models

# Create your models here.
class UserGroup(models.Model):
    uid=models.AutoField(primary_key=True)
    capthion=models.CharField(max_length=32,help_text="数字字母下划线")
    ctime=models.DateTimeField(auto_now_add=True,null=True)
    uptime=models.DateTimeField(auto_now=True,null=True)
    # user_type_choices=(
    #     (1,"超级用户"),
    #     (2, "普通用户"),
    #     (3, "垃圾用户"),
    # )
    # user_type_id=models.IntegerField(choices=user_type_choices,default=1)
class UserInfo(models.Model):
    #用户名列，字符串类型，指定长度
    user_name=models.CharField(max_length=32)
    user_pwd=models.CharField(max_length=64)
    user_tel=models.CharField(max_length=20)
    user_email=models.CharField(max_length=40)
    user_gender=models.CharField(max_length=40,null=True)
    user_group=models.ForeignKey("UserGroup",on_delete="CASCADE",to_field="uid",default=1)