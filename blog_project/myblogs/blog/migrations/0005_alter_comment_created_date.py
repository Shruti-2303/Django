# Generated by Django 3.2 on 2021-06-24 11:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210624_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 24, 11, 42, 44, 286370, tzinfo=utc)),
        ),
    ]