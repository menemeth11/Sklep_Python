# Generated by Django 4.0.4 on 2022-04-11 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.CreateModel(
            name='Producenci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=60)),
                ('opis', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Producent',
                'verbose_name_plural': 'Producenci',
            },
        ),
        migrations.CreateModel(
            name='Stan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=60)),
                ('opis', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Stan',
                'verbose_name_plural': 'Stany',
            },
        ),
        migrations.AlterModelOptions(
            name='produkty',
            options={'verbose_name': 'Produkt', 'verbose_name_plural': 'Produkty'},
        ),
        migrations.AddField(
            model_name='produkty',
            name='kategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.kategorie'),
        ),
        migrations.AddField(
            model_name='produkty',
            name='producent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.producenci'),
        ),
        migrations.AddField(
            model_name='produkty',
            name='stan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.stan'),
        ),
    ]
