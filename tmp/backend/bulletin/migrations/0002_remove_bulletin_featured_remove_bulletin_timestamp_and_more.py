# Generated by Django 4.1.2 on 2022-10-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulletin',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='bulletin',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='overview',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
