# Generated by Django 2.2.2 on 2020-02-04 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_auto_20200204_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='passport',
            field=models.ImageField(blank=True, default='passports/default.jpeg', upload_to='passports'),
        ),
    ]
