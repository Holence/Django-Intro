# Generated by Django 4.2 on 2023-06-08 14:08

import accounts.models
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
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=256, null=True)),
                ('bio', models.TextField(blank=True, max_length=512, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, storage=accounts.models.OverwriteStorage(), upload_to=accounts.models.image_upload_to_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
