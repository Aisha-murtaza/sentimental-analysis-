# Generated by Django 5.0.2 on 2024-05-22 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0007_plan_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plans',
            name='benefit3',
        ),
        migrations.RemoveField(
            model_name='plans',
            name='benefit4',
        ),
    ]