# Generated by Django 4.2.6 on 2023-10-06 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auhor',
            new_name='author',
        ),
    ]
