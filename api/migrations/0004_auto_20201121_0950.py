# Generated by Django 3.1.3 on 2020-11-21 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='handling',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(default='unknown', max_length=255),
            preserve_default=False,
        ),
    ]
