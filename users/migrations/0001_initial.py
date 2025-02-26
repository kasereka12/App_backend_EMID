# Generated by Django 5.0.4 on 2024-07-05 09:56

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Area",
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
                ("area", models.CharField(max_length=250)),
                ("Area_description", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Channels",
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
                ("channel_code", models.CharField(max_length=50)),
                ("Channel_description", models.CharField(max_length=255)),
                ("delivery_system", models.IntegerField()),
                ("related_price_list_code", models.CharField(max_length=50)),
                ("return_price_list_code", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Client_Discounts",
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
                ("Client_Code", models.CharField(max_length=50)),
                ("Trx_Code", models.CharField(max_length=50)),
                ("Discounts", models.DecimalField(decimal_places=2, max_digits=18)),
                ("Month", models.IntegerField()),
                ("Years", models.IntegerField()),
                ("Discounts_label", models.CharField(max_length=50)),
                ("Applied", models.IntegerField()),
                ("Stamp_Date", models.DateTimeField()),
                ("Affected_item_code", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Client_Statut",
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
                ("Client_Statut_ID", models.IntegerField()),
                ("Statut_Description", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Client_Target",
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
                ("Client_Code", models.CharField(max_length=50)),
                ("Month", models.IntegerField()),
                ("years", models.IntegerField()),
                ("Target_value", models.DecimalField(decimal_places=2, max_digits=18)),
                (
                    "Targed_Achieved",
                    models.DecimalField(decimal_places=2, max_digits=18),
                ),
                ("Stamp_Date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Clients",
            fields=[
                (
                    "Client_Code",
                    models.AutoField(default="", primary_key=True, serialize=False),
                ),
                ("Area_Code", models.CharField(blank=True, default="", max_length=50)),
                (
                    "Client_Description",
                    models.CharField(blank=True, default="", max_length=50),
                ),
                (
                    "Client_Alt_Description",
                    models.CharField(blank=True, default="", max_length=50),
                ),
                (
                    "Payment_Term_Code",
                    models.CharField(blank=True, default="", max_length=50),
                ),
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("Address", models.CharField(blank=True, default="", max_length=50)),
                (
                    "Alt_Address",
                    models.CharField(blank=True, default="", max_length=50),
                ),
                (
                    "Contact_Person",
                    models.CharField(blank=True, default="", max_length=50),
                ),
                (
                    "Phone_Number",
                    models.CharField(blank=True, default="", max_length=50),
                ),
                ("Barcode", models.CharField(blank=True, default="", max_length=50)),
                ("Client_Status_ID", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "Clients",
            },
        ),
        migrations.CreateModel(
            name="InternalUser",
            fields=[
                (
                    "UserCode",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("UserName", models.CharField(max_length=100)),
                ("PhoneNumber", models.CharField(blank=True, max_length=15, null=True)),
                ("Grouping", models.CharField(blank=True, max_length=50, null=True)),
                ("IsBlocked", models.BooleanField(default=False)),
                ("LoginName", models.CharField(max_length=100)),
                ("AreaCode", models.CharField(blank=True, max_length=10, null=True)),
                ("CityID", models.IntegerField(blank=True, null=True)),
                ("RouteCode", models.CharField(blank=True, max_length=10, null=True)),
                ("ParentCode", models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                "db_table": "users",
            },
        ),
        migrations.CreateModel(
            name="Parameters",
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
                ("ParameterName", models.CharField(max_length=100)),
                ("DefaultValue", models.CharField(max_length=100)),
                ("ParameterType", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "User_Parameters",
            },
        ),
        migrations.CreateModel(
            name="PromoAssignments",
            fields=[
                ("org_id", models.IntegerField()),
                (
                    "assignment_code",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("assignment_type", models.CharField(max_length=50)),
                ("second_assignment_type", models.CharField(max_length=50)),
                ("second_assignment_code", models.CharField(max_length=50)),
                ("stamp_date", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="PromoHeaders",
            fields=[
                ("promotion_id", models.AutoField(primary_key=True, serialize=False)),
                ("promotion_type", models.CharField(max_length=3)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("promotion_description", models.CharField(max_length=100)),
                ("achievement", models.DecimalField(decimal_places=6, max_digits=18)),
                ("target_value", models.DecimalField(decimal_places=6, max_digits=18)),
                ("is_active", models.BooleanField(default=False)),
                ("is_forced", models.BooleanField(default=False)),
                ("parent_id", models.CharField(blank=True, max_length=14, null=True)),
                ("priority", models.IntegerField()),
                ("promotion_apply", models.IntegerField()),
            ],
            options={
                "db_table": "Promo_Headers",
            },
        ),
        migrations.CreateModel(
            name="PromoItemBasketHeaders",
            fields=[
                ("item_basket_id", models.AutoField(primary_key=True, serialize=False)),
                ("item_basket_description", models.CharField(max_length=100)),
                (
                    "creation_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("last_updated_date", models.DateTimeField()),
            ],
            options={
                "db_table": "Promo_Item_Basket_Headers",
            },
        ),
        migrations.CreateModel(
            name="Regions",
            fields=[
                (
                    "Region_Code",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("Org_ID", models.CharField(max_length=50)),
                ("Region_Description", models.CharField(max_length=100)),
                ("Region_Alt_Description", models.CharField(max_length=100)),
                ("Stamp_Date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=150, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("password", models.CharField(max_length=255)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "db_table": "users_customuser",
            },
        ),
        migrations.CreateModel(
            name="Routes",
            fields=[
                ("Route_ID", models.AutoField(primary_key=True, serialize=False)),
                ("Org_ID", models.CharField(max_length=50)),
                ("Branch_Code", models.CharField(max_length=50)),
                ("Route_Description", models.CharField(max_length=100)),
                ("Route_Alt_Description", models.CharField(max_length=100)),
                ("Region_Code", models.CharField(max_length=50)),
                ("Stamp_Date", models.DateTimeField()),
                ("CreateBy", models.CharField(max_length=100)),
                (
                    "user_code",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "Routes",
            },
        ),
        migrations.CreateModel(
            name="Route_Users",
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
                ("Org_ID", models.CharField(max_length=50)),
                ("Stamp_Date", models.DateTimeField()),
                ("Assignment_Type", models.IntegerField()),
                (
                    "User_Code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "Route_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.routes"
                    ),
                ),
            ],
            options={
                "db_table": "Route_Users",
                "unique_together": {("Route_ID", "User_Code", "Org_ID")},
            },
        ),
    ]
