# Generated by Django 5.1 on 2024-08-24 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField()),
                ('text_ans', models.TextField(blank=True, null=True)),
                ('score_ans', models.IntegerField(blank=True)),
            ],
        ),
    ]
