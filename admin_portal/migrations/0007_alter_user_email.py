# Generated by Django 4.1 on 2022-08-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_portal', '0006_alter_organizationmaster_orguser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Email'),
        ),
    ]
