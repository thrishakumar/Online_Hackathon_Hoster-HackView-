# Generated by Django 3.0.5 on 2020-05-26 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_type',
        ),
    ]
