# Generated by Django 3.2.6 on 2022-05-10 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0043_auto_20220510_0542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roadproject',
            old_name='engineering',
            new_name='contract',
        ),
    ]
