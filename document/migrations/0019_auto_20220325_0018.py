# Generated by Django 3.2.6 on 2022-03-25 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0018_deliverables1_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliverables1',
            old_name='annual_target_1',
            new_name='annual_target',
        ),
        migrations.RemoveField(
            model_name='deliverables1',
            name='annual_target_2',
        ),
        migrations.RemoveField(
            model_name='deliverables1',
            name='annual_target_3',
        ),
    ]
