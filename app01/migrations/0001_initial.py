# Generated by Django 2.1.5 on 2019-01-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host_Group',
            fields=[
                ('nid', models.IntegerField(primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Host_list',
            fields=[
                ('nid', models.IntegerField(primary_key=True, serialize=False)),
                ('host_name', models.CharField(db_index=True, max_length=32)),
                ('host_ip', models.GenericIPAddressField(db_index=True)),
                ('host_port', models.IntegerField()),
                ('host_user', models.CharField(max_length=20)),
                ('host_group', models.ForeignKey(default=1, on_delete='CASCADE', to='app01.Host_Group')),
            ],
        ),
        migrations.CreateModel(
            name='Host_Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_name', models.CharField(max_length=32)),
                ('process_mem', models.CharField(max_length=20)),
                ('process_cup', models.CharField(max_length=20)),
                ('process_in_host', models.ForeignKey(default=1, on_delete='CASCADE', to='app01.Host_Group')),
            ],
        ),
    ]