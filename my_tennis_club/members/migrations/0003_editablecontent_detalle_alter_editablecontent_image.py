# Generated by Django 5.0.3 on 2024-08-12 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_editablecontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='editablecontent',
            name='detalle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='editablecontent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
