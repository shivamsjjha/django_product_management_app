# Generated by Django 3.0.3 on 2020-06-18 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20200618_1401'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='blog',
            unique_together={('title', 'slug')},
        ),
    ]
