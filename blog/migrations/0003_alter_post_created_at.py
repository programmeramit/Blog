# Generated by Django 5.1.2 on 2024-11-03 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2024, 11, 3, 8, 37, 53, 927451, tzinfo=datetime.timezone.utc)),
        ),
    ]
