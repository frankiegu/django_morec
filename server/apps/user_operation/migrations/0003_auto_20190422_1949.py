# Generated by Django 2.1.4 on 2019-04-22 19:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_operation', '0002_auto_20190422_1445'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserFavMovie',
            new_name='UserFavorMovie',
        ),
    ]