# Generated by Django 3.2.5 on 2021-08-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='Your bio, you can update it', null=True),
        ),
    ]