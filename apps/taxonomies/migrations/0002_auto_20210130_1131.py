# Generated by Django 3.1.5 on 2021-01-30 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]