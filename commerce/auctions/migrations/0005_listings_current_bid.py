# Generated by Django 4.2.2 on 2023-07-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0004_comments_bids"),
    ]

    operations = [
        migrations.AddField(
            model_name="listings",
            name="current_bid",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
