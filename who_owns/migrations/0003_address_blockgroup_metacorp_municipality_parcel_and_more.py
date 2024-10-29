# Generated by Django 4.1.5 on 2024-08-24 20:06

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('who_owns', '0002_companytype_evictortype_landlordtype_role_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(blank=True, help_text='Complete number, street name, type string, often reconstructed from address ranges, PO Boxes, etc.', max_length=500, null=True)),
                ('start', models.IntegerField(blank=True, help_text='For ranges, start of address range. For single-number addresses, that single number.', null=True)),
                ('end', models.IntegerField(blank=True, help_text='For ranges, end of address range. For single-number addresses, that single number.', null=True)),
                ('body', models.CharField(blank=True, help_text='Street name and address type.', max_length=500, null=True)),
                ('even', models.BooleanField(default=False, help_text='Whether an address is even or odd.')),
                ('muni_str', models.CharField(blank=True, max_length=250, null=True)),
                ('postal', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'address',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BlockGroup',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=2249)),
            ],
            options={
                'db_table': 'block_group',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MetaCorp',
            fields=[
                ('id', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('val', models.IntegerField(blank=True, null=True)),
                ('prop_count', models.IntegerField(null=True)),
                ('unit_count', models.FloatField(null=True)),
                ('area', models.IntegerField(null=True)),
                ('units_per_prop', models.FloatField(null=True)),
                ('val_per_prop', models.FloatField(null=True)),
                ('val_per_area', models.FloatField(null=True)),
                ('company_count', models.IntegerField(null=True)),
                ('evictor_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.evictortype')),
            ],
            options={
                'db_table': 'metacorps_network',
            },
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('muni', models.CharField(max_length=250, null=True, unique=True)),
                ('hns', models.BooleanField(null=True)),
                ('mapc', models.BooleanField(null=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=2249)),
            ],
            options={
                'db_table': 'muni',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False)),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=2249)),
            ],
            options={
                'db_table': 'parcels',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tract',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=2249)),
            ],
            options={
                'db_table': 'tract',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('zip', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('state', models.CharField(blank=True, max_length=10, null=True)),
                ('unambig_state', models.CharField(blank=True, max_length=10, null=True)),
                ('muni_unambig_from', models.CharField(blank=True, max_length=100, null=True)),
                ('muni_unambig_to', models.CharField(blank=True, max_length=100, null=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=2249)),
            ],
            options={
                'db_table': 'zip',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'managed': True},
        ),
        migrations.AddField(
            model_name='person',
            name='inst',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='plaintiff',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.person'),
        ),
        migrations.AlterModelTable(
            name='companytype',
            table='company_type',
        ),
        migrations.AlterModelTable(
            name='person',
            table='person',
        ),
        migrations.AlterModelTable(
            name='role',
            table='role',
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fy', models.IntegerField()),
                ('ls_date', models.DateField(null=True)),
                ('ls_price', models.IntegerField(null=True)),
                ('bld_area', models.IntegerField(null=True)),
                ('res_area', models.IntegerField(null=True)),
                ('units', models.IntegerField()),
                ('bld_val', models.IntegerField()),
                ('lnd_val', models.IntegerField()),
                ('use_code', models.CharField(max_length=20)),
                ('luc', models.CharField(max_length=10)),
                ('ooc', models.BooleanField()),
                ('condo', models.BooleanField()),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.address')),
                ('muni', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.municipality')),
            ],
            options={
                'db_table': 'site',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ParcelPoint',
            fields=[
                ('id', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('block_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.blockgroup')),
                ('muni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.municipality')),
                ('tract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.tract')),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'parcels_point',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('inst', models.BooleanField(null=True)),
                ('trust', models.BooleanField(null=True)),
                ('trustees', models.BooleanField(null=True)),
                ('cosine_group', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.address')),
                ('metacorp', models.ForeignKey(blank=True, help_text='network_group in original data', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.metacorp')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.site')),
            ],
            options={
                'db_table': 'owner',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.address')),
                ('company_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.companytype')),
                ('landlord_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.landlordtype')),
                ('metacorp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.metacorp')),
                ('owner', models.ManyToManyField(related_name='owners', to='who_owns.owner')),
                ('person', models.ManyToManyField(related_name='people', to='who_owns.person')),
            ],
            options={
                'db_table': 'company',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='address',
            name='loc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.parcelpoint'),
        ),
        migrations.AddField(
            model_name='address',
            name='muni',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.municipality'),
        ),
        migrations.AddField(
            model_name='filing',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.address'),
        ),
        migrations.AddField(
            model_name='plaintiff',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='who_owns.company'),
        ),
    ]


