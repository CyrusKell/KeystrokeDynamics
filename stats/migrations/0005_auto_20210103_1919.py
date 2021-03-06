# Generated by Django 3.1.3 on 2021-01-04 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_auto_20210103_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='dwelldataForKeyA',
            field=models.JSONField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='dwelldataForKeyE',
            field=models.JSONField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='dwelldataForKeyI',
            field=models.JSONField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='dwelldataForKeyO',
            field=models.JSONField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='dwelldataForKeyR',
            field=models.JSONField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='flightdataForKeysAN',
            field=models.JSONField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='flightdataForKeysER',
            field=models.JSONField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='flightdataForKeysHE',
            field=models.JSONField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='flightdataForKeysIN',
            field=models.JSONField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='flightdataForKeysTH',
            field=models.JSONField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='percentsWhenAccepted',
            field=models.JSONField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='percentsWhenDenied',
            field=models.JSONField(blank=True, default='[]'),
        ),
    ]
