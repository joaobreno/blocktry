# Generated by Django 4.1.2 on 2022-11-04 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0002_mail_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mail',
            name='message',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mail',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mail',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]
