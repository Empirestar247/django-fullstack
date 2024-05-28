# Generated by Django 5.0.4 on 2024-05-21 13:19

import apptracker.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('trackingid', models.CharField(default='', max_length=10, null=True)),
                ('Date', models.DateField(default=django.utils.timezone.now)),
                ('Time', models.TimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('Date_of_Departure', models.DateField(default=django.utils.timezone.now)),
                ('expected_delivery', models.DateTimeField(default=django.utils.timezone.now)),
                ('Sender_Name', models.CharField(max_length=400)),
                ('Sender_Origin', models.CharField(max_length=200)),
                ('From', models.CharField(max_length=400)),
                ('To', models.CharField(max_length=400)),
                ('quantity', models.IntegerField()),
                ('customer', models.CharField(max_length=50)),
                ('shipment_address', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('Reciver_Phone', models.CharField(max_length=200)),
                ('Item_Description', models.CharField(max_length=200)),
                ('Weight_And_Dimension', models.TextField(blank=True)),
                ('delicate_item', models.BooleanField()),
                ('fast_delivery', models.BooleanField()),
                ('shipping_charge', models.IntegerField(blank=True, default=0, editable=False)),
                ('tracking_id', models.CharField(blank=True, default=apptracker.models.generate_tracking_id, editable=False, max_length=10)),
                ('status', models.CharField(choices=[('processing', 'Processing'), ('on_the_way', 'On the way'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled'), ('returned', 'Returned'), ('delayed', 'Delayed')], default='processing', max_length=20)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptracker.items')),
            ],
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('tracking_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('processing', 'Processing'), ('on_the_way', 'On the way'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled'), ('returned', 'Returned'), ('delayed', 'Delayed')], max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptracker.shipment')),
            ],
        ),
    ]
