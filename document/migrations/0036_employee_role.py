# Generated by Django 3.2.6 on 2022-04-04 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0035_auto_20220401_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True),
        ),
    ]
