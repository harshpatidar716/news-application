# Generated by Django 4.1.5 on 2023-07-24 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_upload_news_username_alter_upload_news_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report_image',
            name='key',
            field=models.CharField(default='harsh', max_length=50),
        ),
        migrations.AlterField(
            model_name='upload_news',
            name='created_date',
            field=models.DateField(default=datetime.date(2023, 7, 24)),
        ),
        migrations.AlterField(
            model_name='upload_news',
            name='modify_date',
            field=models.DateField(default=datetime.date(2023, 7, 24)),
        ),
    ]
