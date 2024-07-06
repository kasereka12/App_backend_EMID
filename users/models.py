from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Custom user manager for users_customers
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


# CustomUser model for users_customers
class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'users_customuser'

    def __str__(self):
        return self.username


# Model for internal user management in the 'users' table
class InternalUser(models.Model):
    UserCode = models.CharField(max_length=50, primary_key=True)
    UserName = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=15, null=True, blank=True)
    Grouping = models.CharField(max_length=50, null=True, blank=True)
    IsBlocked = models.BooleanField(default=False)
    LoginName = models.CharField(max_length=100)
    AreaCode = models.CharField(max_length=10, null=True, blank=True)
    CityID = models.IntegerField(null=True, blank=True)
    RouteCode = models.CharField(max_length=10, null=True, blank=True)
    ParentCode = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.UserName


class Regions(models.Model):
    Region_Code = models.CharField(max_length=50, primary_key=True)
    Org_ID = models.CharField(max_length=50)
    Region_Description = models.CharField(max_length=100)
    Region_Alt_Description = models.CharField(max_length=100)
    Stamp_Date = models.DateTimeField()

    def __str__(self):
        return self.Region_Description


class Parameters(models.Model):
    ParameterName = models.CharField(max_length=100)
    DefaultValue = models.CharField(max_length=100)
    ParameterType = models.CharField(max_length=50)

    class Meta:
        db_table = 'User_Parameters'

    def __str__(self):
        return self.ParameterName
class Routes(models.Model):
    Route_ID = models.AutoField(primary_key=True)
    Org_ID = models.CharField(max_length=50)
    Branch_Code = models.CharField(max_length=50)
    Route_Description = models.CharField(max_length=100)
    Route_Alt_Description = models.CharField(max_length=100)
    Region_Code = models.CharField(max_length=50)
    Stamp_Date = models.DateTimeField()
    user_code = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, null=True)
    CreateBy = models.CharField(max_length=100)

    class Meta:
        db_table = 'Routes'

class Route_Users(models.Model):
    Route_ID = models.ForeignKey('Routes', on_delete=models.CASCADE)
    User_Code = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    Org_ID = models.CharField(max_length=50)
    Stamp_Date = models.DateTimeField()
    Assignment_Type = models.IntegerField()

    class Meta:
        db_table = 'Route_Users'
        unique_together = ('Route_ID', 'User_Code', 'Org_ID')

class Clients(models.Model):
    Client_Code = models.AutoField(primary_key=True)
    Area_Code = models.CharField(max_length=50, blank=True, default='')
    Client_Description = models.CharField(max_length=50, blank=True, default='')
    Client_Alt_Description = models.CharField(max_length=50, blank=True, default='')
    Payment_Term_Code = models.CharField(max_length=50, blank=True, default='')
    Email = models.EmailField(unique=True)
    Address = models.CharField(max_length=50, blank=True, default='')
    Alt_Address = models.CharField(max_length=50, blank=True, default='')
    Contact_Person = models.CharField(max_length=50, blank=True, default='')   
    Phone_Number = models.CharField(max_length=50, blank=True, default='')
    Barcode = models.CharField(max_length=50, blank=True, default='')
    Client_Status_ID = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(2)])
       

    class Meta:
        
        db_table = 'Clients'


    def __str__(self):
        return self.Client_Description

class PromoHeaders(models.Model):
        promotion_id = models.AutoField(primary_key=True)
        promotion_type = models.CharField(max_length=3)
        start_date = models.DateTimeField()
        end_date = models.DateTimeField()
        promotion_description = models.CharField(max_length=100)
        achievement = models.DecimalField(max_digits=18, decimal_places=6)
        target_value = models.DecimalField(max_digits=18, decimal_places=6)
        is_active = models.BooleanField(default=False)
        is_forced = models.BooleanField(default=False)
        parent_id = models.CharField(max_length=14, null=True, blank=True)
        priority = models.IntegerField()
        promotion_apply = models.IntegerField()

        def __str__(self):
            return f'{self.promotion_description} ({self.promotion_id})'

        class Meta:
            db_table = 'Promo_Headers'

from django.utils import timezone

class PromoAssignments(models.Model):
    org_id = models.IntegerField()
    assignment_code = models.CharField(max_length=50, primary_key=True)
    assignment_type = models.CharField(max_length=50)
    second_assignment_type = models.CharField(max_length=50)
    second_assignment_code = models.CharField(max_length=50)
    stamp_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.assignment_code

class PromoItemBasketHeaders(models.Model):
    item_basket_id = models.AutoField(primary_key=True)
    item_basket_description = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=timezone.now)
    last_updated_date = models.DateTimeField()

    class Meta:
        db_table = 'Promo_Item_Basket_Headers'

    def __str__(self):
        return self.item_basket_description

class Area(models.Model):
    area = models.CharField(max_length=250)
    Area_description = models.CharField(max_length=255)

class Client_Statut(models.Model):
    Client_Statut_ID = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    Statut_Description = models.CharField(max_length=50)

class Client_Discounts(models.Model):
    Client_Code = models.CharField(max_length=50)
    Trx_Code = models.CharField(max_length=50)
    Discounts = models.DecimalField(max_digits=18,decimal_places=2)
    Month = models.IntegerField()
    Years = models.IntegerField()
    Discounts_label = models.CharField(max_length=50)
    Applied = models.IntegerField()
    Stamp_Date = models.DateTimeField()
    Affected_item_code = models.CharField(max_length=50)

class Client_Target(models.Model):
    Client_Code = models.CharField(max_length=50)
    Month = models.IntegerField()
    years = models.IntegerField()
    Target_value = models.DecimalField(max_digits=18,decimal_places=2)
    Targed_Achieved = models.DecimalField(max_digits=18,decimal_places=2)
    Stamp_Date = models.DateTimeField()

class Channels(models.Model):
    channel_code = models.CharField(max_length=50)
    Channel_description = models.CharField(max_length=255)
    delivery_system = models.IntegerField()
    related_price_list_code = models.CharField(max_length=50)
    return_price_list_code = models.CharField(max_length=50)

