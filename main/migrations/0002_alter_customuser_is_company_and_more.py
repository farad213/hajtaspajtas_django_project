# Generated by Django 4.1.2 on 2022-11-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_company',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_private_person',
            field=models.BooleanField(null=True),
        ),
    ]
