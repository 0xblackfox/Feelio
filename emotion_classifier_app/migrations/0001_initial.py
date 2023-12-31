# Generated by Django 4.2.1 on 2023-09-05 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('album', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
            ],
        ),
    ]
