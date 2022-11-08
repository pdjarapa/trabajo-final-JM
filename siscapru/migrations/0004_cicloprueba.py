# Generated by Django 4.1.3 on 2022-11-08 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siscapru', '0003_alter_casoprueba_codigo_alter_casoprueba_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CicloPrueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=80)),
                ('descripcion', models.TextField(blank=True, max_length=250, null=True, verbose_name='Descripción')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ciclos_prueba', to='siscapru.proyecto')),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
    ]
