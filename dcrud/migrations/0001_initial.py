# Generated by Django 4.1.7 on 2023-06-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
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
                ("create_date", models.DateTimeField(auto_now_add=True)),
                ("Description", models.CharField(max_length=100)),
                ("Proposal_amount", models.IntegerField()),
                ("Provision_availed", models.IntegerField()),
                ("PartyName", models.CharField(max_length=100)),
            ],
        ),
    ]
