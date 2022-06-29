# Generated by Django 3.1.2 on 2021-03-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0004_auto_20210325_1331"),
    ]

    operations = [
        migrations.AddField(
            model_name="slot",
            name="type",
            field=models.CharField(
                choices=[
                    ("MEMBERSLOT", "Memberslot"),
                    ("COMPSLOT", "Compslot"),
                    ("GAMESLOT", "Gameslot"),
                    ("COURSESLOT", "Courseslot"),
                    ("EVENTSLOT", "Eventslot"),
                ],
                default="MEMBERSLOT",
                max_length=50,
                verbose_name="Type",
            ),
        ),
        migrations.AlterField(
            model_name="newuser",
            name="type",
            field=models.CharField(
                choices=[
                    ("MEMBER", "Member"),
                    ("COORDINATOR", "Coordinator"),
                    ("COMMITTEE", "Committee"),
                    ("MANAGER", "Manager"),
                ],
                default="MEMBER",
                max_length=50,
                verbose_name="Type",
            ),
        ),
    ]
