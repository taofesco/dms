# Generated by Django 3.2.6 on 2022-04-01 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0029_villagemaintenancecost'),
    ]

    operations = [
        migrations.AddField(
            model_name='pbmc',
            name='road',
            field=models.CharField(max_length=500, null=True),
        ),
    ]