# Generated by Django 2.2.8 on 2020-01-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hooby_app', '0002_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
    ]
