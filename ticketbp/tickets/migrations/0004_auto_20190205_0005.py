# Generated by Django 2.1.3 on 2019-02-04 15:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0003_auto_20190204_2357'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookmarkAnswer',
            new_name='BestAnswer',
        ),
        migrations.AlterModelTable(
            name='bestanswer',
            table='best_answer',
        ),
    ]