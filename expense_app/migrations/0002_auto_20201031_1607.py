# Generated by Django 3.1.2 on 2020-10-31 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='budget',
            field=models.IntegerField(),
        ),
    ]
