# Generated by Django 4.0.3 on 2022-12-27 13:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciperequirement',
            name='unit',
            field=models.ForeignKey(default='kg', on_delete=django.db.models.deletion.CASCADE, related_name='recipe_unit', to='inventory.ingredient'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.FloatField(max_length=30),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='reciperequirement',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingredient', to='inventory.ingredient'),
        ),
    ]
