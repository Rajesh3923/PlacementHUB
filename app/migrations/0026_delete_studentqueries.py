# Generated by Django 4.2.4 on 2023-10-19 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_rename_studentquery_studentqueries'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentQueries',
        ),
    ]
