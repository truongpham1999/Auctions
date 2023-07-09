# Generated by Django 4.2.2 on 2023-07-02 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0005_listings_current_bid"),
    ]

    operations = [
        migrations.AddField(
            model_name="bids",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="comments",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
