# Generated by Django 5.0.3 on 2024-04-30 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url_field',
            field=models.URLField(null=True),
        ),
    ]
