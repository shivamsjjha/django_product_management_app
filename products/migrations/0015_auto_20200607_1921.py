# Generated by Django 3.0.3 on 2020-06-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='body',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
