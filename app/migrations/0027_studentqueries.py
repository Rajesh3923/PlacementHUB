# Generated by Django 4.2.4 on 2023-10-19 02:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_delete_studentqueries'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentQueries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('query', models.TextField()),
                ('mobile', models.IntegerField(default=0)),
                ('arrival_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
