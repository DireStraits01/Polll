# Generated by Django 2.2.10 on 2021-02-28 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poll_app', '0005_auto_20210228_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='anonymus',
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
