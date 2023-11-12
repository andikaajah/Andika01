from django.db import models


class Foto(models.Model):
  foto = models.CharField(max_length=100)
  keterangan = models.TextField()
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.foto}"
  
class Fotoproduk(models.Model):
  nama = models.CharField(max_length=100)


  def __str__(self):
    return f"{self.nama}"