# Generated by Django 3.1.2 on 2021-03-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0009_newuser_acardnum"),
    ]

    operations = [
        migrations.AddField(
            model_name="newuser",
            name="comp_participated",
            field=models.IntegerField(default=0, verbose_name="comp_participated"),
        ),
    ]
