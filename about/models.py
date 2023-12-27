from django.db import models

# Create your models here.



class Induk(models.Model):
    nama_induk = models.CharField(max_length=100)
  

    def __str__(self):
        return f"{self.nama_induk}"

class Anak(models.Model):
    Induk = models.ForeignKey(Induk, on_delete=models.CASCADE)
    jenis = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    umur = models.IntegerField()

    def __str__(self):
        return f"{self.jenis}"


