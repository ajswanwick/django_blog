# Generated by Django 4.2.17 on 2024-12-09 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Post',
            new_name='post',
        ),
    ]
