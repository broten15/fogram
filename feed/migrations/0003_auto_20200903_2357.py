# Generated by Django 3.1 on 2020-09-04 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='test_pic.png', upload_to=''),
        ),
    ]
