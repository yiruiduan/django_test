# Generated by Django 2.1.5 on 2019-01-10 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_usergroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
