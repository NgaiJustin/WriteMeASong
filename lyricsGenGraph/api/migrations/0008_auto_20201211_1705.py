# Generated by Django 3.1.4 on 2020-12-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201211_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyrics', models.CharField(default='', max_length=10000)),
                ('genre', models.CharField(max_length=7)),
                ('length', models.IntegerField(default=-1)),
            ],
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Pop',
        ),
        migrations.DeleteModel(
            name='Rap',
        ),
        migrations.DeleteModel(
            name='Rock',
        ),
        migrations.DeleteModel(
            name='Xmas',
        ),
    ]
