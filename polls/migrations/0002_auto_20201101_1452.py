# Generated by Django 3.1.2 on 2020-11-01 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='Nom',
            new_name='nom',
        ),
    ]
