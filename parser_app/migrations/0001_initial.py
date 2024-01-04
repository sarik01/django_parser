# Generated by Django 5.0 on 2023-12-31 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MeasureUnits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CompoundIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parser_app.groups')),
                ('ingredients', models.ManyToManyField(to='parser_app.ingredients')),
                ('measurement_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parser_app.measureunits')),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalTableCI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calculation_qty', models.FloatField()),
                ('sum', models.FloatField()),
                ('quantity', models.FloatField()),
                ('compound_ingredients', models.ManyToManyField(to='parser_app.compoundingredients')),
                ('ingredients', models.ManyToManyField(to='parser_app.ingredients')),
            ],
        ),
        migrations.AddField(
            model_name='ingredients',
            name='measurement_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parser_app.measureunits'),
        ),
    ]