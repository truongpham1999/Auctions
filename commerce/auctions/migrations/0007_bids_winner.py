# Generated by Django 4.2.2 on 2023-07-03 07:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0006_bids_date_comments_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="bids",
            name="winner",
            field=models.BooleanField(default=False),
        ),
    ]