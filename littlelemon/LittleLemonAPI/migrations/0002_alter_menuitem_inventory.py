# Generated by Django 5.1.2 on 2024-10-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='inventory',
            field=models.IntegerField(),
        ),
    ]
