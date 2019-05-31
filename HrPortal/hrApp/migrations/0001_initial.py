# Generated by Django 2.2.1 on 2019-05-29 14:54

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('CvResume', models.FileField(blank=True, upload_to='')),
                ('catagory', multiselectfield.db.fields.MultiSelectField(choices=[('Quality Assurence', 'Quality Assurence'), ('Developer', 'Developer'), ('Project Manager', 'Project Manager'), ('Data Analyst', 'Data Analyst'), ('Front End(UI/UX)', 'Front End(UI/UX)')], max_length=200)),
                ('motivation', models.CharField(max_length=500)),
            ],
        ),
    ]
