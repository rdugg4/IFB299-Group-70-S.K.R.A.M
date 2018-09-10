# Generated by Django 2.1.1 on 2018-09-10 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_makename', models.CharField(db_column='Car_MakeName', max_length=255)),
                ('car_model', models.CharField(db_column='Car_Model', max_length=255)),
                ('car_series', models.CharField(db_column='Car_Series', max_length=255)),
                ('car_seriesyear', models.IntegerField(db_column='Car_SeriesYear')),
                ('car_pricenew', models.IntegerField(db_column='Car_PriceNew')),
                ('car_enginesize', models.CharField(db_column='Car_EngineSize', max_length=255)),
                ('car_fuelsystem', models.CharField(db_column='Car_FuelSystem', max_length=255)),
                ('car_tankcapacity', models.CharField(db_column='Car_TankCapacity', max_length=255)),
                ('car_power', models.CharField(db_column='Car_Power', max_length=255)),
                ('car_seatingcapacity', models.IntegerField(db_column='Car_SeatingCapacity')),
                ('car_standardtransmission', models.CharField(db_column='Car_StandardTransmission', max_length=255)),
                ('car_bodytype', models.CharField(db_column='Car_BodyType', max_length=255)),
                ('car_drive', models.CharField(db_column='Car_Drive', max_length=3)),
                ('car_wheelbase', models.CharField(db_column='Car_Wheelbase', max_length=255)),
            ],
            options={
                'db_table': 'cars',
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=20, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
                ('dob', models.CharField(blank=True, db_column='DOB', max_length=20, null=True)),
                ('occupation', models.CharField(blank=True, db_column='Occupation', max_length=255, null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=3, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=255, null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=255, null=True)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('createdate', models.IntegerField(blank=True, db_column='CreateDate', null=True)),
                ('pickupdate', models.IntegerField(blank=True, db_column='PickupDate', null=True)),
                ('returndate', models.IntegerField(blank=True, db_column='ReturnDate', null=True)),
                ('droppedoff', models.CharField(blank=True, db_column='DroppedOff', max_length=255, null=True)),
                ('carid', models.ForeignKey(blank=True, db_column='CarID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='testApp.Cars')),
                ('customerid', models.ForeignKey(blank=True, db_column='CustomerID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='testApp.Customers')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=20, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=255, null=True)),
                ('state', models.CharField(blank=True, db_column='State', max_length=255, null=True)),
            ],
            options={
                'db_table': 'stores',
            },
        ),
        migrations.AddField(
            model_name='orders',
            name='pickupstore',
            field=models.ForeignKey(blank=True, db_column='PickupStore', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pickupStore', to='testApp.Stores'),
        ),
        migrations.AddField(
            model_name='orders',
            name='returnstore',
            field=models.ForeignKey(blank=True, db_column='ReturnStore', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='returnStore', to='testApp.Stores'),
        ),
    ]
