# Generated by Django 4.1.6 on 2023-02-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("announcements", "0002_auto_20200629_0826"),
    ]

    operations = [
        migrations.AddField(
            model_name="announcement",
            name="send_email",
            field=models.BooleanField(
                default=False,
                help_text="Send an email to all users in the group. If no group is selected, this is ignored.",
            ),
        ),
    ]
