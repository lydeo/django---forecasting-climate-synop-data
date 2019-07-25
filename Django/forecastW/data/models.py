from django.db import models

class data_klimat(models.Model):
    bulan= models.CharField(max_length=40)
    temp_rata2= models.FloatField(null=True)
    temp_max= models.FloatField(null=True)
    temp_min=models.FloatField(null=True)
    curah_hujan=models.FloatField(null=True)
    penyinaran_matahari= models.FloatField(null=True)
    tekanan_udara= models.FloatField(null=True)
    kelembaban=models.FloatField(null=True)
    kec_rata_angin= models.FloatField(null=True)
    tahun= models.CharField(max_length=4, null=True)

class indeks_musiman(models.Model):
    bulan= models.CharField(max_length=40)
    temp_rata2= models.FloatField(null=True)
    temp_max= models.FloatField(null=True)
    temp_min=models.FloatField(null=True)
    curah_hujan=models.FloatField(null=True)
    penyinaran_matahari= models.FloatField(null=True)
    tekanan_udara= models.FloatField(null=True)
    kelembaban=models.FloatField(null=True)
    kec_rata_angin= models.FloatField(null=True)
    
