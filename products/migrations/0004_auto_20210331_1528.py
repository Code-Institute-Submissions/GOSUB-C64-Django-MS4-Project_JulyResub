# Generated by Django 3.1.7 on 2021-03-31 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_customer_printables'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Printables',
            new_name='Print_Media',
        ),
    ]
