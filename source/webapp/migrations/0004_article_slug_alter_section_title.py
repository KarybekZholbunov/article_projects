# Generated by Django 5.0.6 on 2024-07-14 14:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_section_remove_article_update_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, unique=True, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
