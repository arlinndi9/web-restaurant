# Generated by Django 4.1.7 on 2023-03-28 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('subject', models.TextField(default='')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=230)),
                ('email', models.EmailField(max_length=254)),
                ('time', models.CharField(default='', max_length=12)),
                ('phone', models.CharField(default='', max_length=30)),
                ('people', models.IntegerField(default='')),
                ('message', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]