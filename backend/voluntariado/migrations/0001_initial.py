# Generated by Django 3.1.3 on 2020-11-16 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbVoluntariado',
            fields=[
                ('voluntariado_id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_voluntariado', models.CharField(max_length=100)),
                ('desc_voluntariado', models.TextField()),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voluntariados', to='pessoas.tbpessoa')),
            ],
            options={
                'verbose_name': 'Voluntariado',
                'verbose_name_plural': 'Voluntariados',
            },
        ),
    ]
