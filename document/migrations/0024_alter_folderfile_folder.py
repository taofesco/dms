# Generated by Django 3.2.6 on 2022-03-25 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0023_alter_folder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folderfile',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='folder_file', to='document.folder'),
        ),
    ]
