# Generated by Django 3.1.4 on 2020-12-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyrics', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Pop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyrics', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Rap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyrics', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Rock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyrics', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Xmas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyrics', models.CharField(max_length=10000)),
            ],
        ),
    ]
