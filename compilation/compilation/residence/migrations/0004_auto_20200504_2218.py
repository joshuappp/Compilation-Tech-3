# Generated by Django 3.0.5 on 2020-05-04 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residence', '0003_auto_20200504_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadroom',
            name='image',
            field=models.ImageField(default=False, upload_to='compilation/home/static/img/residence/'),
            preserve_default=False,
        ),
    ]