# Generated by Django 4.1.3 on 2022-11-14 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_adddata_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddata',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 14, 11, 21, 50, 138837)),
        ),
    ]
