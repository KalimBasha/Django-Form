# Generated by Django 3.2.25 on 2024-11-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('Scid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Sname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Stid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Stname', models.CharField(max_length=200)),
                ('loc', models.CharField(max_length=50)),
                ('Mobile', models.PositiveIntegerField()),
            ],
        ),
    ]
