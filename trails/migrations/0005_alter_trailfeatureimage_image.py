# Generated by Django 4.2 on 2024-10-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0004_trailfeatureimage_image_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailfeatureimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='trail_features/'),
        ),
    ]
