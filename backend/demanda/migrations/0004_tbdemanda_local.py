# Generated by Django 3.1.3 on 2020-11-16 16:40

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demanda', '0003_remove_tbdemanda_servico'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbdemanda',
            name='local',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
