# Generated by Django 2.0.7 on 2018-07-11 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-create_time',)},
        ),
    ]
