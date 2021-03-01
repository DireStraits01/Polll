# Generated by Django 2.2.10 on 2021-02-28 12:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('is_multiple_choice', models.BooleanField()),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll_app.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll_app.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2021, 2, 28), editable=False)),
                ('Option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll_app.Option')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll_app.Poll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll_app.Question')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
