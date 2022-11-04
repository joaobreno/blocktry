# Generated by Django 4.1.2 on 2022-10-30 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_contract', models.CharField(max_length=200)),
                ('email', models.TextField()),
                ('date_contract', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('photo_contract', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y')),
                ('cpf', models.CharField(max_length=11)),
                ('role', models.TextField()),
            ],
        ),
    ]
