# Generated by Django 4.1.5 on 2023-04-09 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='birth',
            field=models.DateField(default='1111/11/11', max_length=50),
        ),
    ]
