# Generated by Django 3.2.6 on 2021-09-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210910_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_percent',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True),
        ),
    ]
