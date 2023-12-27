from django.db import models

# Create your models here.


class Person(models.Model):
    nama_person = models.CharField(max_length=100)
    jenis = models.CharField(max_length=100,)
    umur = models.CharField(max_length=100)
    def _str_(self):
        return f"{self.nama_person}"


class Jamil(models.Model):
    Person = models.ForeignKey("Person", on_delete=models.CASCADE)
    pekerjaan = models.CharField(max_length=100)
    status = models.TextField()

    def _str_(self):
        return f"{self.pekerjaan}"