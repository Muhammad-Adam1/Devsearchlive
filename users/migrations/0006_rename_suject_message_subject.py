# Generated by Django 4.2.5 on 2023-10-05 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='suject',
            new_name='subject',
        ),
    ]