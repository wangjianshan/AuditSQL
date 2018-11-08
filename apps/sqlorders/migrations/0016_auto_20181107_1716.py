# Generated by Django 2.1.2 on 2018-11-07 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlorders', '0015_auto_20181107_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysqlschemas',
            name='is_master',
        ),
        migrations.AddField(
            model_name='mysqlschemas',
            name='is_type',
            field=models.SmallIntegerField(choices=[(0, '查询_只读'), (1, 'SQL审核'), (2, '查询_读写')], default=0, verbose_name='用途'),
        ),
    ]