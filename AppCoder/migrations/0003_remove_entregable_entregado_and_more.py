# Generated by Django 4.2.3 on 2023-07-13 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_rename_nombre_entregable_entrega'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entregable',
            name='entregado',
        ),
        migrations.RemoveField(
            model_name='entregable',
            name='fecha_entrega',
        ),
    ]
