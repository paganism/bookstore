# Generated by Django 2.1.3 on 2018-12-01 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20181201_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genregroups',
            name='parent_group',
            field=models.ForeignKey(blank=True, default=-1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.GenreGroups'),
        ),
    ]
