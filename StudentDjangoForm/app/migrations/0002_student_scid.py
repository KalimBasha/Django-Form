# Generated by Django 3.2.25 on 2024-11-05 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Scid',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='app.school'),
            preserve_default=False,
        ),
    ]
