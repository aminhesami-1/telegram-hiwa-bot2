# Generated by Django 5.0.6 on 2024-06-30 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_alter_appointment_user'),
        ('basic_user', '0005_basic_user_is_user_verifyed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basic_user.basic_user'),
        ),
    ]
