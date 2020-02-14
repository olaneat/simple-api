# Generated by Django 2.1.4 on 2020-02-14 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Execursion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('data_page_name', models.SlugField(max_length=200)),
                ('port_id', models.CharField(max_length=100)),
                ('trip_type', models.CharField(max_length=50)),
                ('typology', models.CharField(choices=[(29, 29), (84, 84)], max_length=200)),
                ('activity_level', models.CharField(max_length=150)),
                ('collectionType', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('en', 'en'), ('fr', 'fr'), ('Gr', 'Gr')], max_length=20)),
                ('price_level', models.CharField(max_length=20)),
                ('currency', models.CharField(max_length=10)),
                ('meal_info', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=15)),
                ('short_description', models.CharField(max_length=150)),
                ('long_description', models.TextField()),
                ('external_content', models.BooleanField(default=False)),
                ('minimum_age', models.CharField(max_length=15)),
                ('wheel_chair_accessible', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Execursion',
                'verbose_name_plural': 'Execursions',
                'ordering': ('name',),
            },
        ),
    ]