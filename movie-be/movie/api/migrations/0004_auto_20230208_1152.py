# Generated by Django 3.0.7 on 2023-02-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20230208_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movierating',
        ),
        migrations.AddField(
            model_name='movie',
            name='watchrating',
            field=models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R')], default='G', max_length=10),
        ),
    ]