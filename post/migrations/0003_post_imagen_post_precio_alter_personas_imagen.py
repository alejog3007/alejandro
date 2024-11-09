# Generated by Django 5.1.1 on 2024-10-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_personas_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='post',
            name='precio',
            field=models.FloatField(default=True),
        ),
        migrations.AlterField(
            model_name='personas',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]