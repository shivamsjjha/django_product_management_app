# Generated by Django 3.0.3 on 2020-06-10 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_quotepics'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DiscountField',
        ),
        migrations.DeleteModel(
            name='Places',
        ),
    ]