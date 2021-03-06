# Generated by Django 2.1.3 on 2018-12-01 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20181128_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreDepends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GenreGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter genre group name', max_length=150)),
                ('parent_id', models.ForeignKey(default=-1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.GenreGroups')),
            ],
        ),
        migrations.AddField(
            model_name='genredepends',
            name='genre_group_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.GenreGroups'),
        ),
        migrations.AddField(
            model_name='genredepends',
            name='genre_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Genre'),
        ),
    ]
