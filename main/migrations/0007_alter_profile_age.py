# Generated by Django 4.1.3 on 2022-12-14 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_profile_firstname_alter_profile_lastname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="age",
            field=models.IntegerField(null=True),
        ),
    ]
