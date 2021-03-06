# Generated by Django 3.2.6 on 2022-03-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=500, null=True)),
                ('annual_budget', models.CharField(max_length=500, null=True)),
                ('approraited_budget', models.CharField(max_length=500, null=True)),
                ('preventive_maintenace', models.CharField(max_length=500, null=True)),
                ('planned_maintenace', models.CharField(max_length=500, null=True)),
                ('routine_maintenace', models.CharField(max_length=500, null=True)),
                ('emergency_works', models.CharField(max_length=500, null=True)),
                ('other_activities', models.CharField(max_length=500, null=True)),
                ('released_budget', models.CharField(max_length=500, null=True)),
                ('utilized_budget', models.CharField(max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(blank=True, choices=[('Periodic', 'Periodic'), ('Routine', 'Routine')], max_length=20, null=True)),
                ('level', models.CharField(blank=True, choices=[('Federal', 'Federal'), ('State', 'State'), ('LGA:Rural', 'LGA:Rural'), ('LGA:Urban', 'LGA:Urban')], max_length=20, null=True)),
                ('dual_carriage_amount', models.IntegerField(null=True)),
                ('dual_carriage_percent', models.IntegerField(null=True)),
                ('single_carriage_amount', models.IntegerField(null=True)),
                ('single_carriage_percent', models.IntegerField(null=True)),
                ('earth_carriage_amount', models.IntegerField(null=True)),
                ('earth_carriage_percent', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='company_photo',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='role',
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_no',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='level',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='position_management',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='technical',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='title',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
