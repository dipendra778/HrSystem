# Generated by Django 2.2.1 on 2019-05-31 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='motivation',
            field=models.CharField(max_length=1000),
        ),
    ]
