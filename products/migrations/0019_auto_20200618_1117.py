# Generated by Django 3.0.3 on 2020-06-18 05:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200610_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=500)),
                ('author', models.CharField(default='Unknown', max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='youtube')),
                ('post', models.TextField()),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='youtube')),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='quotepics',
            name='author',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='quotepics',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
