# Generated by Django 4.2.7 on 2023-12-24 13:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_order_email_id_order_status_alter_order_table_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="email_id",
        ),
    ]