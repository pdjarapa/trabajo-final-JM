# Generated by Django 4.1.3 on 2022-11-17 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siscapru', '0007_remove_casoprueba_observacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejecucionprueba',
            name='proyecto',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ejecucion_pruebas', to='siscapru.proyecto'),
            preserve_default=False,
        ),
    ]
