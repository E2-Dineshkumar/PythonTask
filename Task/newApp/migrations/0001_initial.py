# Generated by Django 4.1 on 2022-10-11 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('standard', models.CharField(max_length=3)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
