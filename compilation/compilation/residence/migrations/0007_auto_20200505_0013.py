# Generated by Django 3.0.5 on 2020-05-05 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residence', '0006_auto_20200504_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadroom',
            name='image',
            field=models.ImageField(upload_to='home/static/img/residence/'),
        ),
    ]