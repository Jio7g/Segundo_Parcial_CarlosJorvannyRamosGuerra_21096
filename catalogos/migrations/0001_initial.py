# Generated by Django 4.2.5 on 2023-09-23 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=9, unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
