# Generated by Django 5.1 on 2024-09-19 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('viewed_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.file')),
            ],
        ),
    ]
