# Generated by Django 5.0.3 on 2024-03-31 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo_me',
            field=models.ImageField(blank=True, upload_to='photos/my_photo'),
        ),
    ]
