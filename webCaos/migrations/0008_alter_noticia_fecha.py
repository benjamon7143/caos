# Generated by Django 4.2.1 on 2023-06-08 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webCaos', '0007_categoria_foto_alter_noticia_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='Fecha',
            field=models.DateField(verbose_name=datetime.date(2023, 6, 8)),
        ),
    ]