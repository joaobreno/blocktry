# Generated by Django 4.1.2 on 2022-10-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contract',
            name='role',
            field=models.CharField(max_length=200),
        ),
    ]