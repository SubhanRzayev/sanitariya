# Generated by Django 3.2.4 on 2021-08-25 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(upload_to='media/services_image')),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
