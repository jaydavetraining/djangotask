# Generated by Django 4.2.13 on 2024-06-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0002_alter_news_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(),
        ),
    ]