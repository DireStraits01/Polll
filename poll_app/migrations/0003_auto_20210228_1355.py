# Generated by Django 2.2.10 on 2021-02-28 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0002_auto_20210228_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='date',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='option',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='question',
            name='is_multiple_choice',
        ),
        migrations.AddField(
            model_name='answer',
            name='many_options',
            field=models.ManyToManyField(null=True, to='poll_app.Option'),
        ),
        migrations.AddField(
            model_name='answer',
            name='one_option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='option', to='poll_app.Option'),
        ),
        migrations.AddField(
            model_name='answer',
            name='text_input',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='poll_type',
            field=models.CharField(choices=[('free_text', 'free text input'), ('option', 'only one choice'), ('options', 'many choices')], default='default_type', max_length=50, verbose_name='Types of polls'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poll',
            name='description',
            field=models.TextField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=250),
        ),
    ]
