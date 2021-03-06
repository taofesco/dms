# Generated by Django 3.2.6 on 2022-03-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0010_rename_roadinformantion_roadinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryRoad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('route_no', models.IntegerField(null=True)),
                ('total_length', models.IntegerField(null=True)),
                ('cway_width', models.IntegerField(null=True)),
                ('shoulder_width', models.IntegerField(null=True)),
                ('wc', models.IntegerField(null=True)),
                ('bc', models.IntegerField(null=True)),
                ('sd', models.IntegerField(null=True)),
                ('earth', models.IntegerField(null=True)),
                ('sub_base', models.CharField(max_length=500, null=True)),
                ('base', models.CharField(max_length=500, null=True)),
                ('shoulder', models.CharField(max_length=500, null=True)),
                ('good', models.IntegerField(null=True)),
                ('fair', models.IntegerField(null=True)),
                ('poor', models.IntegerField(null=True)),
                ('bad', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Legend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asphaltic_concrete', models.IntegerField(null=True)),
                ('wc', models.IntegerField(null=True)),
                ('sd', models.IntegerField(null=True)),
                ('earth', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NonRoadProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('works', models.IntegerField(null=True)),
                ('good_services', models.IntegerField(null=True)),
                ('consultancy', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMaintenanceWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mda', models.CharField(max_length=500, null=True)),
                ('description', models.CharField(max_length=1500, null=True)),
                ('contract_no', models.IntegerField(null=True)),
                ('contractor', models.CharField(max_length=500, null=True)),
                ('contract_sum', models.IntegerField(null=True)),
                ('amount_appropriated', models.IntegerField(null=True)),
                ('release', models.IntegerField(null=True)),
                ('amount_certified', models.IntegerField(null=True)),
                ('amount_paid', models.IntegerField(null=True)),
                ('outstanding_amount', models.IntegerField(null=True)),
                ('compl', models.IntegerField(null=True)),
                ('remark', models.TextField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoadProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('east_west', models.IntegerField(null=True)),
                ('engineering', models.IntegerField(null=True)),
                ('diralables', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good', models.CharField(max_length=500, null=True)),
                ('fair', models.CharField(max_length=500, null=True)),
                ('poor', models.CharField(max_length=500, null=True)),
                ('bad', models.CharField(max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
