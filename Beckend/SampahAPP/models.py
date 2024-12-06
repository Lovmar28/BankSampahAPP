from django.db import models

# Create your models here.
class TitikPoin(models.Model):
    Nama_TitikPoin = models.CharField(max_length=30)
    Pemilik_TitikPoin = models.CharField(max_length=30)
    Telpon_TitikPoin = models.CharField(max_length=13)
    Alamat_TitikPoin = models.TextField()

    def __str__(self):
        return self.Nama_TitikPoin

class Sampah(models.Model):
    Jenis_Sampah = [('O','Organik'),('A','Anorganik')]
    Nama_Sampah = models.CharField(max_length=30)
    Jenis_Sampah = models.CharField(max_length=10, choices=Jenis_Sampah)
    Harga_Sampah = models.IntegerField()

    def __str__(self):
        return self.Nama_Sampah
    
class User(models.Model):
    Nama_User = models.CharField(max_length=50)
    Email_User = models.EmailField()
    Username = models.CharField(max_length=10)
    Password = models.CharField(max_length=10)
    Alamat_User = models.TextField()
    Telpon_User = models.CharField(max_length=13)
    
    def __str__(self):
        return self.Nama_User

class Setor(models.Model):
    Jumlah_Setor = models.IntegerField()
    Tanggal_Setor = models.DateTimeField()
    Nama_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='DataUser_setor')
    Nama_TitikPoin = models.ForeignKey(TitikPoin, on_delete=models.CASCADE, related_name='DataTitikPoin_setor')
    Nama_Sampah = models.ForeignKey(Sampah, on_delete=models.CASCADE, related_name='DataSampah_setor')

    def __str__(self):
        return self.Jumlah_Setor

class Tabungan(models.Model):
    Saldo_Tabungan = models.IntegerField()
    Nama_User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='DataUser_tabungan')

    def __str__(self):
        return self.Saldo_Tabungan


class Tarik(models.Model):
    Jumlah_Tarik = models.IntegerField()
    Tanggal_Tarik = models.DateTimeField()
    Nama_User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='DataUser_tarik')
    Nama_Tabungan = models.ForeignKey(Tabungan, on_delete=models.CASCADE, related_name='DataTabungan_tarik')

    def __str__(self):
        return self.Tanggal_Tarik

class Contact_Us(models.Model):
    Nama_Pengirim = models.CharField(max_length=50)
    Email_Pengirim = models.EmailField()
    Saran_Pengirim = models.TextField()

    def __str__(self):
        return self.Nama_Pengirim
    
class Admin(models.Model):
    Username_Admin = models.CharField(max_length=10)
    Password_Admin = models.CharField(max_length=10)

    def __str__(self):
        return self.Username_Admin