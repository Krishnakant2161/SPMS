# Generated by Django 3.1.2 on 2021-03-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="newuser",
            name="city",
            field=models.CharField(
                default="Kharagpur", max_length=15, null=True, verbose_name="city"
            ),
        ),
        migrations.AddField(
            model_name="newuser",
            name="country",
            field=models.CharField(
                default="India", max_length=15, null=True, verbose_name="country"
            ),
        ),
    ]
