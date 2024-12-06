# Generated by Django 5.1.2 on 2024-11-29 07:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username_Admin', models.CharField(max_length=10)),
                ('Password_Admin', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_Pengirim', models.CharField(max_length=50)),
                ('Email_Pengirim', models.EmailField(max_length=254)),
                ('Saran_Pengirim', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sampah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_Sampah', models.CharField(max_length=30)),
                ('Jenis_Sampah', models.CharField(choices=[('O', 'Organik'), ('A', 'Anorganik')], max_length=10)),
                ('Harga_Sampah', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tabungan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Saldo_Tabungan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TitikPoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_TitikPoin', models.CharField(max_length=30)),
                ('Pemilik_TitikPoin', models.CharField(max_length=30)),
                ('Telpon_TitikPoin', models.CharField(max_length=13)),
                ('Alamat_TitikPoin', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_User', models.CharField(max_length=50)),
                ('Email_User', models.EmailField(max_length=254)),
                ('Username', models.CharField(max_length=10)),
                ('Password', models.CharField(max_length=10)),
                ('Alamat_User', models.TextField()),
                ('Telpon_User', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Tarik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jumlah_Tarik', models.IntegerField()),
                ('Tanggal_Tarik', models.DateTimeField()),
                ('Nama_Tabungan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DataTabungan_tarik', to='SampahAPP.tabungan')),
                ('Nama_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DataUser_tarik', to='SampahAPP.user')),
            ],
        ),
        migrations.AddField(
            model_name='tabungan',
            name='Nama_User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DataUser_tabungan', to='SampahAPP.user'),
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jumlah_Setor', models.IntegerField()),
                ('Tanggal_Setor', models.DateTimeField()),
                ('Nama_Sampah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DataSampah_setor', to='SampahAPP.sampah')),
                ('Nama_TitikPoin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DataTitikPoin_setor', to='SampahAPP.titikpoin')),
                ('Nama_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DataUser_setor', to='SampahAPP.user')),
            ],
        ),
    ]