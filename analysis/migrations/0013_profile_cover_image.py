# Generated by Django 5.0.2 on 2024-05-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0012_rename_username_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_image',
            field=models.ImageField(default='media/user.jpg', null=True, upload_to='profile_images/'),
        ),
    ]