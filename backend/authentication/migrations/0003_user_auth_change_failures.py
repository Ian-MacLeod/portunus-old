# Generated by Django 3.0.7 on 2020-07-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_user_social_login_provider"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="auth_change_failures",
            field=models.IntegerField(default=0),
        ),
    ]
