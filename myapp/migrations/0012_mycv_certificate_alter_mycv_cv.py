# Generated by Django 4.0.6 on 2022-08-31 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycv',
            name='certificate',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='mycv',
            name='cv',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
    ]
