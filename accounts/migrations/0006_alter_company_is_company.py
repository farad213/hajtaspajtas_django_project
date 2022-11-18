# Generated by Django 4.1.2 on 2022-11-18 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_customuser_is_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='is_company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]