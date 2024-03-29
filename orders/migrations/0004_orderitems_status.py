# Generated by Django 4.2.7 on 2023-12-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0003_remove_order_email_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitems",
            name="status",
            field=models.CharField(
                choices=[("ordered", "Ordered"), ("shipped", "Shipped")],
                default="ordered",
                max_length=20,
            ),
        ),
    ]
