# Generated by Django 3.2 on 2021-04-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='brak'),
            preserve_default=False,
        ),
    ]