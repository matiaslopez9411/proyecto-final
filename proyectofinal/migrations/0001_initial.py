# Generated by Django 4.1.3 on 2022-12-08 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jedi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('numero_jedi', models.IntegerField()),
                ('titulo', models.CharField(max_length=200)),
                ('color_sable', models.CharField(max_length=200)),
            ],
        ),
    ]
