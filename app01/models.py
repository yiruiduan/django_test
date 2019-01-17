from django.db import models

# Create your models here.
class Host_Group(models.Model):
    nid=models.AutoField(primary_key=True)
    caption=models.CharField(max_length=32)

class Host_List(models.Model):
    nid=models.AutoField(primary_key=True)
    host_name=models.CharField(max_length=32,db_index=True)
    host_ip=models.GenericIPAddressField(db_index=True)
    host_port=models.IntegerField()
    host_user=models.CharField(max_length=20)
    host_group=models.ForeignKey("Host_Group",on_delete="CASCADE",to_field="nid",default=1)
    class Meta:
        unique_together =["host_name","host_ip"]

class Host_Process(models.Model):
    process_name=models.CharField(max_length=32)
    process_mem=models.CharField(max_length=20)
    process_cpu=models.CharField(max_length=20)
    process_in_host=models.ForeignKey("Host_List",on_delete="CASCADE",to_field="nid",default=1)

class Application(models.Model):
    app_name=models.CharField(max_length=32)
    r= models.ManyToManyField("Host_List")

# class Host_To_Application(models.Model):
#     hobj=models.ForeignKey("Host_List",on_delete="CASCADE",to_field="nid")
#     aobj=models.ForeignKey("Application",on_delete="CASCADE",to_field="id")

