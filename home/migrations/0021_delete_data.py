# Generated by Django 4.1.5 on 2023-03-29 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_data_birth_remove_data_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='data',
        ),
    ]