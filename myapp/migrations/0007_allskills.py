# Generated by Django 4.0.6 on 2022-08-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill1', models.CharField(blank=True, max_length=300)),
                ('percentage', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
