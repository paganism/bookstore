# Generated by Django 2.1.3 on 2018-12-01 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20181201_1008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genredepends',
            old_name='genre_id',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='genredepends',
            old_name='genre_group_id',
            new_name='genre_group',
        ),
        migrations.RenameField(
            model_name='genregroups',
            old_name='parent_id',
            new_name='parent_group',
        ),
    ]