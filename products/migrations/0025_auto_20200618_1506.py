# Generated by Django 3.0.3 on 2020-06-18 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20200618_1434'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Channel',
        ),
        migrations.DeleteModel(
            name='Quotepics',
        ),
    ]
