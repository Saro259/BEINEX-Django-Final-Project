# Generated by Django 4.2.7 on 2023-12-02 08:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tags", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, unique=True)),
                ("slug", models.CharField(max_length=250, unique=True)),
                ("description", models.TextField(null=True)),
                ("price", models.IntegerField(default=0)),
                ("quantity", models.IntegerField(default=0)),
                ("image", models.URLField(max_length=2048)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("tags", models.ManyToManyField(blank=True, to="tags.tags")),
            ],
            options={
                "db_table": "products",
            },
        ),
    ]
