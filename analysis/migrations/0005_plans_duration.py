# Generated by Django 5.0.2 on 2024-04-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_alter_plans_plan_pricing'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='duration',
            field=models.IntegerField(null=True),
        ),
    ]