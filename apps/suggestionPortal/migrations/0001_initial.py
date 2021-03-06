# Generated by Django 3.1.7 on 2021-04-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("mysite", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="id"
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                ("text", models.CharField(max_length=500, verbose_name="text")),
                (
                    "reply",
                    models.CharField(
                        default="Thanks for your feedback",
                        max_length=500,
                        verbose_name="reply",
                    ),
                ),
                ("replied", models.BooleanField(default=False, verbose_name="replied")),
                ("date", models.DateField(blank=True, null=True, verbose_name="date")),
                (
                    "persons",
                    models.ManyToManyField(
                        blank=True, related_name="persons", to="mysite.NewUser"
                    ),
                ),
                (
                    "user",
                    models.ManyToManyField(related_name="user", to="mysite.NewUser"),
                ),
            ],
        ),
    ]
