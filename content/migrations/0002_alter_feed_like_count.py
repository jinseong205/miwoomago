# Generated by Django 4.0.3 on 2022-04-13 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='like_count',
            field=models.IntegerField(),
        ),
    ]
