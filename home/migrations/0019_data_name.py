# Generated by Django 4.1.5 on 2023-03-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_data_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='name',
            field=models.CharField(default='null', max_length=50),
        ),
    ]