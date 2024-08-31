# Generated by Django 5.1 on 2024-08-31 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_level', models.CharField(max_length=100)),
                ('establishment_type', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
