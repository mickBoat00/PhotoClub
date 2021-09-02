# Generated by Django 3.2.5 on 2021-08-24 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Photo', '0003_alter_comment_commenter_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commenter_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]