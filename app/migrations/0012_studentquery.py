# Generated by Django 4.2.4 on 2023-10-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('query', models.TextField()),
            ],
        ),
    ]
