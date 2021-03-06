# Generated by Django 3.0.5 on 2020-05-11 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '0005_auto_20200510_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qa1', models.TextField()),
                ('qa2', models.TextField()),
                ('qa3', models.TextField()),
                ('qa4', models.TextField()),
                ('qa5', models.TextField()),
                ('qa6', models.TextField()),
                ('applyers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('challenge', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='challenges.Challenges')),
            ],
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
