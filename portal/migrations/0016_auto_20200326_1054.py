# Generated by Django 2.2.2 on 2020-03-26 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_courses'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
    ]