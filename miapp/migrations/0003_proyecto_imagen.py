# Generated by Django 5.0.2 on 2025-02-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_mensajecontacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='proyectos/'),
        ),
    ]
