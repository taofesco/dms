# Generated by Django 3.2.6 on 2022-04-04 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0038_alter_employee_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='employee/'),
        ),
    ]
