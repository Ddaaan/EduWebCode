# Generated by Django 5.1 on 2024-09-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='school_id',
            field=models.CharField(default='default_id', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='school_pw',
            field=models.CharField(default='default_pw', max_length=100),
            preserve_default=False,
        ),
    ]
