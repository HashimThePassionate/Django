# Generated by Django 4.2.6 on 2023-11-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('librarian', models.CharField(max_length=50)),
                ('books', models.CharField(max_length=50)),
                ('library_card', models.CharField(max_length=50)),
                ('wifi', models.BooleanField()),
            ],
        ),
    ]