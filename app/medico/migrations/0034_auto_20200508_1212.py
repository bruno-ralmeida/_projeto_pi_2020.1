# Generated by Django 3.0.5 on 2020-05-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0033_auto_20200508_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/1588950727.5107481'),
        ),
    ]
