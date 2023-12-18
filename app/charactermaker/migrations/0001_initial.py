# Generated by Django 4.2.6 on 2023-11-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128)),
                ('sex', models.CharField(blank=True, max_length=128)),
                ('age', models.IntegerField(blank=True)),
                ('description', models.CharField(blank=True, max_length=10000)),
                ('backstory', models.CharField(blank=True, max_length=10000)),
                ('level', models.IntegerField()),
            ],
        ),
    ]