# Generated by Django 3.1.7 on 2021-04-04 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("compPage", "0001_initial"),
        ("mysite", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="user",
            field=models.ManyToManyField(to="mysite.NewUser"),
        ),
        migrations.AddField(
            model_name="game",
            name="competition",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="compPage.competition",
            ),
        ),
    ]
