# Generated by Django 2.1.1 on 2018-10-05 00:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GestiRED', '0004_auto_20181004_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fase',
            name='fechaInicial',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='fechaRegistro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='resource',
            name='fechaRegistro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='fechaRegistro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
