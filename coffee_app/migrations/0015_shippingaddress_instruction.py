# Generated by Django 3.2.9 on 2021-12-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_app', '0014_alter_shippingaddress_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='instruction',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
