# Generated by Django 2.2.10 on 2021-02-28 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0006_auto_20210228_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='many_options',
            field=models.ManyToManyField(to='poll_app.Option'),
        ),
    ]
