# Generated by Django 5.1.3 on 2024-11-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('age', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('size', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('age_limited', models.BooleanField(default=False)),
                ('buyer', models.ManyToManyField(to='task1.buyer')),
            ],
        ),
    ]
