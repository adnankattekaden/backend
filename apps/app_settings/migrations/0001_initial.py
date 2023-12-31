# Generated by Django 4.2 on 2023-04-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ResponseCodes",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.IntegerField()),
                ("title", models.CharField(max_length=30)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Active"), (1, "Inactive")], default=0
                    ),
                ),
            ],
        ),
    ]
