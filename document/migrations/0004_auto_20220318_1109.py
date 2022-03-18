# Generated by Django 3.2.6 on 2022-03-18 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20220318_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='annual_budget',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='approraited_budget',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='emergency_works',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='other_activities',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='planned_maintenance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='preventive_maintenance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='released_budget',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='routine_maintenance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='utilized_budget',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
