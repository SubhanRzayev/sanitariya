# Generated by Django 3.2.4 on 2021-08-26 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='description',
            field=models.CharField(default='Write the text', max_length=1000),
        ),
    ]
