# Generated by Django 4.0.6 on 2022-08-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_education_year_month_alter_education_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='services',
            name='logo',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='service_title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
