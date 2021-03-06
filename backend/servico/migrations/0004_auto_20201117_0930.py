# Generated by Django 3.1.3 on 2020-11-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariado', '0001_initial'),
        ('oferta', '0002_auto_20201117_0921'),
        ('servico', '0003_auto_20201117_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbservico',
            name='oferta',
            field=models.ManyToManyField(related_name='servicos', to='oferta.TbOferta'),
        ),
        migrations.AddField(
            model_name='tbservico',
            name='voluntariado',
            field=models.ManyToManyField(related_name='voluntariados', to='voluntariado.TbVoluntariado'),
        ),
    ]
