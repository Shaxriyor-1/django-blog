# Generated by Django 4.1.4 on 2022-12-19 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_basemodel_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
