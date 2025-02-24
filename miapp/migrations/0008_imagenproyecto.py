# Generated by Django 5.1.6 on 2025-02-23 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0007_testimonio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenProyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='proyectos/')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='miapp.proyecto')),
            ],
        ),
    ]
