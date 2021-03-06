# Generated by Django 3.2.9 on 2021-11-20 12:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=50)),
                ('craet_at', models.DateTimeField(default=datetime.datetime(2021, 11, 20, 12, 24, 57, 167296, tzinfo=utc))),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
