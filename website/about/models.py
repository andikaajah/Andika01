from django.db import models


class Produk(models.Model):
  nama = models.CharField(max_length=100)
  keterangan = models.TextField()

  def __str__(self):
    return f"{self.nama}"
  
class Katagori(models.Model):
  nama = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.nama}"