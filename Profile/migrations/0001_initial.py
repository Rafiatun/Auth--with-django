# Generated by Django 3.2.6 on 2021-08-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=60)),
                ('Last_Name', models.CharField(max_length=60)),
                ('Institution', models.CharField(max_length=60)),
            ],
        ),
    ]
