# Generated by Django 4.0.4 on 2022-08-15 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_rename_content_text_news_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='body',
            new_name='content_text',
        ),
    ]
