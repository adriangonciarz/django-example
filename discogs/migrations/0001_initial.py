# Generated by Django 2.2.6 on 2019-11-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(choices=[('pl', 'Poland'), ('us', 'United States'), ('uk', 'United Kingdom'), ('other', 'Other')], max_length=255)),
            ],
        ),
    ]
