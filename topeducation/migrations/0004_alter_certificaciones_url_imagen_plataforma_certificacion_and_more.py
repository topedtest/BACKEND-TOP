# Generated by Django 5.1.2 on 2024-10-24 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topeducation', '0003_alter_certificaciones_empresa_certificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificaciones',
            name='url_imagen_plataforma_certificacion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='certificaciones',
            name='url_imagen_universidad_certificacion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
