# Generated by Django 2.2.2 on 2020-02-04 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_auto_20200204_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='passport',
            field=models.ImageField(blank=True, default='passports/default.jpg', upload_to='passports'),
        ),
    ]