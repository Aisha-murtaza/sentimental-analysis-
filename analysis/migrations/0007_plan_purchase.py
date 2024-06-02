# Generated by Django 5.0.2 on 2024-05-05 18:52

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0006_alter_plans_options_alter_user_result_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan_purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=50)),
                ('plan_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('plan_expired', models.IntegerField(default=32)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PlanBuy', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Purchase Plans',
            },
        ),
    ]