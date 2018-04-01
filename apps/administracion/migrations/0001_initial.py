# Generated by Django 2.0.2 on 2018-03-23 01:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BitacoraEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=12)),
                ('fecha', models.DateField(default=datetime.datetime.today)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(blank=True, max_length=10, unique=True)),
                ('sueldo', models.FloatField(blank=True)),
                ('fecha_nacimiento', models.DateField(blank=True, default=None, null=True)),
                ('direccion', models.CharField(blank=True, max_length=80)),
                ('telefono', models.CharField(blank=True, max_length=14)),
                ('rol', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregar', models.BooleanField()),
                ('eliminar', models.BooleanField()),
                ('editar', models.BooleanField()),
                ('actualizar', models.BooleanField()),
                ('suspender', models.BooleanField()),
                ('habilitar', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='permisos',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='administracion.Permisos'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bitacoraempleado',
            name='user',
            field=models.ForeignKey(default=None, on_delete='cascade', to='administracion.Empleado'),
        ),
    ]
