# Generated by Django 3.0.5 on 2020-04-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0024_auto_20200428_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/1588092886.7371728'),
        ),
    ]