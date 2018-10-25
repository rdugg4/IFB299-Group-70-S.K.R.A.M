# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Cars(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    car_makename = models.CharField(db_column='Car_MakeName', max_length=255)  # Field name made lowercase.
    car_model = models.CharField(db_column='Car_Model', max_length=255)  # Field name made lowercase.
    car_series = models.CharField(db_column='Car_Series', max_length=255)  # Field name made lowercase.
    car_seriesyear = models.IntegerField(db_column='Car_SeriesYear')  # Field name made lowercase.
    car_pricenew = models.IntegerField(db_column='Car_PriceNew')  # Field name made lowercase.
    car_enginesize = models.CharField(db_column='Car_EngineSize', max_length=255)  # Field name made lowercase.
    car_fuelsystem = models.CharField(db_column='Car_FuelSystem', max_length=255)  # Field name made lowercase.
    car_tankcapacity = models.CharField(db_column='Car_TankCapacity', max_length=255)  # Field name made lowercase.
    car_power = models.CharField(db_column='Car_Power', max_length=255)  # Field name made lowercase.
    car_seatingcapacity = models.IntegerField(db_column='Car_SeatingCapacity')  # Field name made lowercase.
    car_standardtransmission = models.CharField(db_column='Car_StandardTransmission', max_length=255)  # Field name made lowercase.
    car_bodytype = models.CharField(db_column='Car_BodyType', max_length=255)  # Field name made lowercase.
    car_drive = models.CharField(db_column='Car_Drive', max_length=3)  # Field name made lowercase.
    car_wheelbase = models.CharField(db_column='Car_Wheelbase', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'cars'

class Customers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dob = models.CharField(db_column='DOB', max_length=20, blank=True, null=True)  # Field name made lowercase.
    occupation = models.CharField(db_column='Occupation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=3, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'customers'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)

class Stores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'stores'

class StaffMembers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    storeid = models.ForeignKey(Stores, models.DO_NOTHING, db_column='StoreID', blank=True, null=True)

class Orders(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    createdate = models.IntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    pickupdate = models.IntegerField(db_column='PickupDate', blank=True, null=True)  # Field name made lowercase.
    pickupstore = models.ForeignKey('Stores', models.DO_NOTHING, db_column='PickupStore', blank=True, null=True, related_name='pickupStore')  # Field name made lowercase.
    returndate = models.IntegerField(db_column='ReturnDate', blank=True, null=True)  # Field name made lowercase.
    returnstore = models.ForeignKey('Stores', models.DO_NOTHING, db_column='ReturnStore', blank=True, null=True, related_name='returnStore')  # Field name made lowercase.
    droppedoff = models.CharField(db_column='DroppedOff', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    carid = models.ForeignKey(Cars, models.DO_NOTHING, db_column='CarID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'orders'
