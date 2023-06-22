# Generated by Django 4.1.5 on 2023-03-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_data_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='data',
            name='email',
        ),
        migrations.RemoveField(
            model_name='data',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='data',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='data',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='data',
            name='midlename',
        ),
        migrations.RemoveField(
            model_name='data',
            name='phone',
        ),
        migrations.AlterField(
            model_name='data',
            name='name',
            field=models.CharField(default='harsh', max_length=50),
        ),
        migrations.AlterField(
            model_name='data',
            name='password',
            field=models.CharField(default='harsh', max_length=50),
        ),
    ]