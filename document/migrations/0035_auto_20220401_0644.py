# Generated by Django 3.2.6 on 2022-04-01 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0034_stakeholder_other'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summaryscorecard',
            name='q1_2021',
        ),
        migrations.RemoveField(
            model_name='summaryscorecard',
            name='q2_2021',
        ),
        migrations.RemoveField(
            model_name='summaryscorecard',
            name='q3_2021',
        ),
        migrations.RemoveField(
            model_name='summaryscorecard',
            name='y_2020',
        ),
        migrations.AddField(
            model_name='summaryscorecard',
            name='q1',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='summaryscorecard',
            name='q2',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='summaryscorecard',
            name='q3',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='summaryscorecard',
            name='q4',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='summaryscorecard',
            name='year',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
