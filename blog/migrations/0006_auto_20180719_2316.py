# Generated by Django 2.0.7 on 2018-07-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_readed_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='readed_num',
        ),
        migrations.AddField(
            model_name='blog',
            name='read_num',
            field=models.IntegerField(default=0, verbose_name='阅读量'),
        ),
    ]
