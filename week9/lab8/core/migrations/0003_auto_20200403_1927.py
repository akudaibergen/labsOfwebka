# Generated by Django 3.0.5 on 2020-04-03 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catygory_id',
            new_name='category_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='descriprion',
            new_name='description',
        ),
    ]
