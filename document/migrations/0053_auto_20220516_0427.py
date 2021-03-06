# Generated by Django 3.2.6 on 2022-05-16 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0052_countryinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='correction_works',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='inventoryroad',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='kpi',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='legend',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='managementplan',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='nonroadasset',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pbmc',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pestle',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='publicprivatepartnership',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='roadasset',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='roadinformation',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='roadmaintenanceimpact',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='roadproject',
            name='location',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='summaryscorecard',
            name='date',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='deliverables1',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='deliverables2',
            name='q1_actual',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='deliverables2',
            name='q1_target',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='deliverables2',
            name='q2_actual',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='deliverables2',
            name='q2_target',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='deliverables2',
            name='q3_actual',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='deliverables2',
            name='q3_target',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='deliverables2',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='summaryscorecard',
            name='length_recovered',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='summaryscorecard',
            name='q1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='summaryscorecard',
            name='q2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='summaryscorecard',
            name='q3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='summaryscorecard',
            name='q4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='summaryscorecard',
            name='range',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='summaryscorecard',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
