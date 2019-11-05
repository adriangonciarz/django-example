# Generated by Django 2.2.6 on 2019-11-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discogs', '0002_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('rock', 'Rock'), ('jazz', 'Jazz'), ('funk', 'Funk'), ('blues', 'Blues'), ('pop', 'Pop')], max_length=100),
        ),
    ]