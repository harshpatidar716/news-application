# Generated by Django 4.1.5 on 2023-07-26 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_remove_report_image_key_report_image_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_image',
            name='id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='home.upload_news'),
        ),
    ]
