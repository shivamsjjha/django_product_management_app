# Generated by Django 3.0.3 on 2020-06-18 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_blog_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='blog',
            unique_together={('title', 'slug')},
        ),
    ]
