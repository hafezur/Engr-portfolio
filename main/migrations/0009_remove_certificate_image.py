# Generated by Django 5.0.3 on 2024-04-29 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_certificate_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='image',
        ),
    ]
