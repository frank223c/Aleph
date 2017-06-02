# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-02 06:18
from __future__ import unicode_literals

import Fondos.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, upload_to=Fondos.models.path_and_rename)),
                ('alias', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(default='Desconocida', max_length=40)),
                ('procedencia', models.CharField(default='Desconocida', max_length=40)),
                ('fnac', models.CharField(default='Desconocida', max_length=14)),
                ('fdef', models.CharField(default='Desconocida', max_length=14)),
                ('refbiografia', models.URLField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Bibliografia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=60)),
                ('anio', models.CharField(max_length=30, verbose_name='A\xf1o la publicacion')),
                ('pagina', models.CharField(max_length=30, verbose_name='P\xe1gina')),
                ('edicion', models.CharField(max_length=10, verbose_name='Edicion')),
                ('extracto', models.TextField(blank=True)),
                ('isbn', models.CharField(blank=True, max_length=13, verbose_name='ISBN')),
                ('url', models.URLField(blank=True, default='', max_length=500)),
            ],
            options={
                'ordering': ['edicion'],
                'verbose_name_plural': 'Bibliografias',
            },
        ),
        migrations.CreateModel(
            name='Cultura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Culturas',
            },
        ),
        migrations.CreateModel(
            name='Donante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('dni', models.CharField(blank=True, max_length=9)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Donantes',
            },
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Iconografia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Iconografia')),
                ('descripcion', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Iconografias',
            },
        ),
        migrations.CreateModel(
            name='InformeArqueo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_res', models.CharField(max_length=30, verbose_name='Nombre restaurador')),
                ('ape_res', models.CharField(max_length=50, verbose_name='Apellidos del restaurador')),
                ('proyecto', models.TextField(verbose_name='Proyecto')),
                ('observaciones', models.TextField(verbose_name='Observaciones extra sobre el objeto')),
                ('desarrollo', models.TextField(verbose_name='Desarrollo')),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha del informe')),
            ],
            options={
                'ordering': ['fecha'],
                'verbose_name_plural': 'Intervenciones de arqueolog\xeda',
            },
        ),
        migrations.CreateModel(
            name='InformeEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_res', models.CharField(max_length=30, verbose_name='Nombre restaurador')),
                ('ape_res', models.CharField(max_length=50, verbose_name='Apellidos del restaurador')),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha del informe de estado')),
                ('cartela', models.TextField()),
                ('marco', models.TextField(blank=True)),
                ('montaje', models.TextField(blank=True)),
                ('muestras', models.BooleanField(default=False)),
                ('obra', models.TextField(blank=True)),
                ('conclusion', models.TextField()),
                ('prioridad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)], verbose_name='Prioridad')),
                ('propuesta', models.TextField()),
                ('metodologia', models.TextField()),
            ],
            options={
                'ordering': ['fecha'],
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Materiales',
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=20, verbose_name='Ciudad')),
                ('museo', models.CharField(max_length=30, verbose_name='Museo')),
                ('nombre_exposicion', models.CharField(max_length=30, verbose_name='Exposicion')),
                ('fecha_prestado', models.DateField()),
                ('fecha_devuelto', models.DateField()),
            ],
            options={
                'ordering': ['fecha_prestado'],
                'verbose_name_plural': 'Movimientos',
            },
        ),
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anverso', models.ImageField(upload_to=Fondos.models.path_and_rename)),
                ('reverso', models.ImageField(upload_to=Fondos.models.path_and_rename)),
                ('codigo', models.CharField(choices=[('DJ', 'DJ'), ('CE', 'CE'), ('DO', 'DO'), ('DE', 'DE')], default='DJ', max_length=2, verbose_name='C\xf3digo')),
                ('numinv', models.IntegerField(default=1, unique=True, verbose_name='N\xfamero de inventario')),
                ('altura', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Altura en cm')),
                ('ancho', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ancho en cm')),
                ('datacion', models.CharField(default='Desconocida', max_length=30, verbose_name='Fecha de la que data el objeto')),
                ('fechaingreso', models.CharField(max_length=30, verbose_name='Fecha de ingreso')),
                ('ubicacionmus', models.CharField(max_length=30, verbose_name='Ubicacion en el museo')),
                ('descripcion', models.TextField()),
                ('observaciones', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Secciones de arqueologia',
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Soporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Tipos de soportes',
            },
        ),
        migrations.CreateModel(
            name='Tecnica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Tipos de tecnicas',
            },
        ),
        migrations.CreateModel(
            name='Yacimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yacimiento', models.CharField(max_length=30)),
                ('municipio', models.CharField(max_length=30)),
                ('localidad', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['yacimiento'],
                'verbose_name_plural': 'Yacimientos de arqueologia',
            },
        ),
        migrations.CreateModel(
            name='Arqueologia',
            fields=[
                ('objeto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Fondos.Objeto')),
                ('nombre', models.CharField(max_length=30)),
                ('hallazgos', models.TextField(blank=True, null=True)),
                ('depositado', models.CharField(max_length=20)),
                ('conservacion', models.CharField(choices=[('1', 'Bueno'), ('2', 'Regular'), ('3', 'Malo')], default='1', max_length=1)),
                ('edad', models.CharField(choices=[('Edad de piedra', 'Edad de piedra'), ('Edad de bronce', 'Edad de bronce'), ('Edad de metal', 'Edad de metal'), ('Edad de hierro', 'Edad de hierro'), ('Edad moderna', 'Edad moderna'), ('Edad de piedra', 'Edad desconocida')], default='Edad desconocida', max_length=17)),
                ('cultura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fondos.Cultura')),
                ('material', models.ManyToManyField(to='Fondos.Material')),
                ('seccion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Fondos.Seccion')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fondos.Serie')),
                ('yacimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fondos.Yacimiento')),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Arqueologia',
            },
            bases=('Fondos.objeto',),
        ),
        migrations.CreateModel(
            name='Bellasartes',
            fields=[
                ('objeto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Fondos.Objeto')),
                ('titulo', models.CharField(max_length=40)),
                ('procedencia', models.CharField(max_length=20)),
                ('formaingreso', models.CharField(choices=[('Compra', 'Compra'), ('Donacion', 'Donacion'), ('Legado', 'Legado')], default='1', max_length=8, verbose_name='Forma de ingreso')),
                ('autor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Fondos.Autor')),
                ('donante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Fondos.Donante')),
                ('iconografia', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Fondos.Iconografia')),
                ('soporte', models.ManyToManyField(to='Fondos.Soporte')),
                ('tecnica', models.ManyToManyField(blank=True, to='Fondos.Tecnica')),
            ],
            options={
                'ordering': ['titulo'],
                'verbose_name_plural': 'Bellas Artes',
            },
            bases=('Fondos.objeto',),
        ),
        migrations.CreateModel(
            name='InformeIntervencion',
            fields=[
                ('estado_rel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Fondos.InformeEstado')),
                ('tipo', models.CharField(max_length=80)),
                ('justificacion', models.TextField(verbose_name='Justificaci\xf3n de la intervencion')),
                ('criterios', models.TextField()),
                ('estudios', models.BooleanField(default=False)),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha del informe de estado')),
                ('priori_des', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)], verbose_name='Prioridad tras intervencion')),
                ('descripcioninter', models.TextField(verbose_name='Descripcion')),
                ('recom', models.TextField(verbose_name='Recomendaciones')),
            ],
            options={
                'ordering': ['fecha'],
                'verbose_name_plural': 'Intervenciones',
            },
        ),
        migrations.AddField(
            model_name='objeto',
            name='bibliografia',
            field=models.ManyToManyField(blank=True, to='Fondos.Bibliografia'),
        ),
        migrations.AddField(
            model_name='objeto',
            name='movimientos',
            field=models.ManyToManyField(blank=True, null=True, to='Fondos.Movimiento'),
        ),
        migrations.AddField(
            model_name='informeestado',
            name='estudio',
            field=models.ManyToManyField(to='Fondos.Estudio', verbose_name='Estudios realizados'),
        ),
        migrations.AddField(
            model_name='informeestado',
            name='objeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fondos.Objeto', verbose_name='Objeto sobre el que se realiza el informe'),
        ),
        migrations.AddField(
            model_name='informearqueo',
            name='objeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fondos.Objeto', verbose_name='Objeto sobre el que se realiza el informe'),
        ),
    ]
