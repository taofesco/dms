# Generated by Django 3.2.6 on 2022-03-25 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0021_file_folder_folderfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folderfile',
            name='file',
            field=models.FileField(upload_to='files/'),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
