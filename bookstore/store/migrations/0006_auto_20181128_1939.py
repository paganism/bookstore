# Generated by Django 2.1.3 on 2018-11-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20181128_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(null=True, upload_to='img/', width_field=180),
        ),
    ]
