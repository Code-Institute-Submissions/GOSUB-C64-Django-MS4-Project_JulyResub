# Generated by Django 3.1.7 on 2021-04-23 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20210422_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='media_type',
            field=models.CharField(choices=[('print_media', 'Print Media'), ('digital_media', 'Digital Media')], default='none', max_length=20),
        ),
    ]
