# Generated by Django 5.2.1 on 2025-06-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('tipo_usuario', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
    ]
