# Generated by Django 5.0.2 on 2024-05-25 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0010_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]