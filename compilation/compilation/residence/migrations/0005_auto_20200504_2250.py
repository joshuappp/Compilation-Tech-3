# Generated by Django 3.0.5 on 2020-05-04 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residence', '0004_auto_20200504_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadroom',
            name='image',
            field=models.FileField(upload_to='compilation/home/static/img/residence/'),
        ),
    ]
