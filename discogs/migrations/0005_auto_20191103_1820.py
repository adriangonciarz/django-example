# Generated by Django 2.2.6 on 2019-11-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discogs', '0004_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]