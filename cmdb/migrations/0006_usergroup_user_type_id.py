# Generated by Django 2.1.5 on 2019-01-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_usergroup_uptime'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='user_type_id',
            field=models.IntegerField(choices=[(1, '超级用户'), (2, '普通用户'), (3, '垃圾用户')], default=1),
        ),
    ]
