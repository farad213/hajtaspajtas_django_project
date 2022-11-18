# Generated by Django 4.1.2 on 2022-11-18 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_company_is_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='is_company',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]