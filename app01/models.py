from django.db import models

# Create your models here.
class Host_Group(models.Model):
    nid=models.IntegerField(primary_key=True)
    caption=models.CharField(max_length=32)

class Host_List(models.Model):
    nid=models.AutoField(primary_key=True)
    host_name=models.CharField(max_length=32,db_index=True)
    host_ip=models.GenericIPAddressField(db_index=True)
    host_port=models.IntegerField()
    host_user=models.CharField(max_length=20)
    host_group=models.ForeignKey("Host_Group",on_delete="CASCADE",to_field="nid",default=1)

class Host_Process(models.Model):
    process_name=models.CharField(max_length=32)
    process_mem=models.CharField(max_length=20)
    process_cpu=models.CharField(max_length=20)
    process_in_host=models.ForeignKey("Host_List",on_delete="CASCADE",to_field="nid",default=1)
