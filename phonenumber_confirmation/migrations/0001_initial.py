# Generated by Django 3.0.5 on 2020-04-03 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('verified', models.BooleanField(default=False, verbose_name='verified')),
                ('primary', models.BooleanField(default=False, verbose_name='primary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_phone', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'phone number ',
                'verbose_name_plural': 'Phone Numbers',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumberConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.IntegerField(max_length=6, unique=True, verbose_name='pin')),
                ('sent', models.DateTimeField(null=True, verbose_name='sent')),
                ('phone_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_number', to='phonenumber_confirmation.PhoneNumber')),
            ],
            options={
                'verbose_name': 'phone number confirmation',
                'verbose_name_plural': 'Phone Number Confirmations',
            },
        ),
    ]
