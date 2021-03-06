# Generated by Django 2.2 on 2019-04-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cergen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('serial_number', models.CharField(max_length=150)),
                ('protocol', models.CharField(max_length=150)),
                ('callibration_data', models.CharField(max_length=150)),
                ('validity', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'ReferenceEquipment',
            },
        ),
    ]
