# Generated by Django 4.0.2 on 2022-06-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_addbook_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbook',
            name='Category',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
