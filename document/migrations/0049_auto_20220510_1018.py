# Generated by Django 3.2.6 on 2022-05-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0048_auto_20220510_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='job_statistics',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='activities',
            name='period',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='kpi',
            name='period',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='summarymaintenance',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
