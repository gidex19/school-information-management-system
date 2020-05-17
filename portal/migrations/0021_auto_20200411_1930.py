# Generated by Django 2.2.2 on 2020-04-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0020_auto_20200410_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject_2',
            name='current_class',
            field=models.CharField(blank=True, choices=[('JSS 1 BLUE', 'JSS 1 BLUE'), ('JSS 1 GREEN', 'JSS 1 GREEN'), ('JSS 1 YELLOW', 'JSS 1 YELLOW'), ('JSS 2 BLUE', 'JSS 2 BLUE'), ('JSS 2 GREEN', 'JSS 2 GREEN'), ('JSS 2 YELLOW', 'JSS 1 YELLOW'), ('JSS 3 BLUE', 'JSS 3 BLUE'), ('JSS 3 GREEN', 'JSS 3 GREEN'), ('JSS 3 YELLOW', 'JSS 3 YELLOW'), ('SSS 1 HARMONY', 'SSS 1 HARMONY'), ('SSS 1 SMART', 'SSS 1 SMART'), ('SSS 1 SPECIAL', 'SSS 1 SPECIAL'), ('SSS 2 HARMONY', 'SSS 2 HARMONY'), ('SSS 2 SMART', 'SSS 2 SMART'), ('SSS 2 SPECIAL', 'SSS 2 SPECIAL'), ('SSS 3 HARMONY', 'SSS 3 HARMONY'), ('SSS 3 SMART', 'SSS 3 SMART'), ('SSS 3 SPECIAL', 'SSS 3 SPECIAL'), ('Graduated', 'Graduated')], max_length=30),
        ),
        migrations.AddField(
            model_name='subject_3',
            name='current_class',
            field=models.CharField(blank=True, choices=[('JSS 1 BLUE', 'JSS 1 BLUE'), ('JSS 1 GREEN', 'JSS 1 GREEN'), ('JSS 1 YELLOW', 'JSS 1 YELLOW'), ('JSS 2 BLUE', 'JSS 2 BLUE'), ('JSS 2 GREEN', 'JSS 2 GREEN'), ('JSS 2 YELLOW', 'JSS 1 YELLOW'), ('JSS 3 BLUE', 'JSS 3 BLUE'), ('JSS 3 GREEN', 'JSS 3 GREEN'), ('JSS 3 YELLOW', 'JSS 3 YELLOW'), ('SSS 1 HARMONY', 'SSS 1 HARMONY'), ('SSS 1 SMART', 'SSS 1 SMART'), ('SSS 1 SPECIAL', 'SSS 1 SPECIAL'), ('SSS 2 HARMONY', 'SSS 2 HARMONY'), ('SSS 2 SMART', 'SSS 2 SMART'), ('SSS 2 SPECIAL', 'SSS 2 SPECIAL'), ('SSS 3 HARMONY', 'SSS 3 HARMONY'), ('SSS 3 SMART', 'SSS 3 SMART'), ('SSS 3 SPECIAL', 'SSS 3 SPECIAL'), ('Graduated', 'Graduated')], max_length=30),
        ),
        migrations.AddField(
            model_name='subjectz',
            name='current_class',
            field=models.CharField(blank=True, choices=[('JSS 1 BLUE', 'JSS 1 BLUE'), ('JSS 1 GREEN', 'JSS 1 GREEN'), ('JSS 1 YELLOW', 'JSS 1 YELLOW'), ('JSS 2 BLUE', 'JSS 2 BLUE'), ('JSS 2 GREEN', 'JSS 2 GREEN'), ('JSS 2 YELLOW', 'JSS 1 YELLOW'), ('JSS 3 BLUE', 'JSS 3 BLUE'), ('JSS 3 GREEN', 'JSS 3 GREEN'), ('JSS 3 YELLOW', 'JSS 3 YELLOW'), ('SSS 1 HARMONY', 'SSS 1 HARMONY'), ('SSS 1 SMART', 'SSS 1 SMART'), ('SSS 1 SPECIAL', 'SSS 1 SPECIAL'), ('SSS 2 HARMONY', 'SSS 2 HARMONY'), ('SSS 2 SMART', 'SSS 2 SMART'), ('SSS 2 SPECIAL', 'SSS 2 SPECIAL'), ('SSS 3 HARMONY', 'SSS 3 HARMONY'), ('SSS 3 SMART', 'SSS 3 SMART'), ('SSS 3 SPECIAL', 'SSS 3 SPECIAL'), ('Graduated', 'Graduated')], max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='current_class',
            field=models.CharField(blank=True, choices=[('JSS 1 BLUE', 'JSS 1 BLUE'), ('JSS 1 GREEN', 'JSS 1 GREEN'), ('JSS 1 YELLOW', 'JSS 1 YELLOW'), ('JSS 2 BLUE', 'JSS 2 BLUE'), ('JSS 2 GREEN', 'JSS 2 GREEN'), ('JSS 2 YELLOW', 'JSS 1 YELLOW'), ('JSS 3 BLUE', 'JSS 3 BLUE'), ('JSS 3 GREEN', 'JSS 3 GREEN'), ('JSS 3 YELLOW', 'JSS 3 YELLOW'), ('SSS 1 HARMONY', 'SSS 1 HARMONY'), ('SSS 1 SMART', 'SSS 1 SMART'), ('SSS 1 SPECIAL', 'SSS 1 SPECIAL'), ('SSS 2 HARMONY', 'SSS 2 HARMONY'), ('SSS 2 SMART', 'SSS 2 SMART'), ('SSS 2 SPECIAL', 'SSS 2 SPECIAL'), ('SSS 3 HARMONY', 'SSS 3 HARMONY'), ('SSS 3 SMART', 'SSS 3 SMART'), ('SSS 3 SPECIAL', 'SSS 3 SPECIAL'), ('Graduated', 'Graduated')], max_length=30),
        ),
    ]
