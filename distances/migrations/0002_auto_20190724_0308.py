# Generated by Django 2.2.3 on 2019-07-24 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distances', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myfile',
            name='file',
        ),
        migrations.AddField(
            model_name='myfile',
            name='dest_pts',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='myfile',
            name='origin_pts',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]