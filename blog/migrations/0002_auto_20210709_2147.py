# Generated by Django 3.2.5 on 2021-07-09 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='artists',
            field=models.TextField(default='sarley joe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='null', upload_to='images/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='lyrics',
            field=models.TextField(default='some lyrics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='src',
            field=models.FileField(default=1, upload_to='audio/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
