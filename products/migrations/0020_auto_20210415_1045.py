# Generated by Django 3.1.7 on 2021-04-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20210415_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digital_media',
            name='name',
            field=models.CharField(choices=[('icon_sets', 'Icon Sets'), ('brand_logos', 'Brand Logos'), ('web_banners', 'Web Banners')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='print_media',
            name='name',
            field=models.CharField(choices=[('business_cards', 'Business Cards'), ('leaflets_flyers', 'Leaflets & Flyers'), ('posters', 'Posters')], default='1', max_length=20),
        ),
    ]
