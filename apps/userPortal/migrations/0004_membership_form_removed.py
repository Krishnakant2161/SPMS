# Generated by Django 3.1.7 on 2021-03-29 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userPortal", "0003_membership_form_reason"),
    ]

    operations = [
        migrations.AddField(
            model_name="membership_form",
            name="removed",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="removed"
            ),
        ),
    ]
