# Generated by Django 5.0.4 on 2024-07-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clients",
            name="Client_Code",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
