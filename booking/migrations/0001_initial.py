# Generated by Django 3.2.19 on 2023-05-29 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(blank=True, max_length=50)),
                ('host_email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.host')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('listing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='booking.listing')),
                ('property_type', models.CharField(max_length=50)),
                ('bed_type', models.CharField(max_length=50)),
                ('room_type', models.CharField(max_length=50)),
                ('environment_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.user')),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('available', models.BooleanField()),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.listing')),
            ],
        ),
    ]
