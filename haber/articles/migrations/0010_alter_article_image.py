# Generated by Django 3.2.4 on 2021-06-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
