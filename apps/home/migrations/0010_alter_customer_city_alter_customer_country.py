# Generated by Django 5.1.1 on 2025-05-02 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_customer_email_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
