# Generated by Django 3.2.6 on 2022-04-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0037_alter_employee_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(blank=True, choices=[('View', 'View'), ('Create', 'Create'), ('Admin', 'Admin')], max_length=20, null=True),
        ),
    ]