from django.db import models

class Kontak(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subtitle = models.CharField(max_length=255)
    description2 = models.TextField()
    description3 = models.TextField()
    subtitle2 = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Kerja(models.Model):
    list = models.CharField(max_length=255)

    def __str__(self):
        return self.list
    
class Alamat(models.Model):
    list = models.CharField(max_length=255)

    def __str__(self):
        return self.list
    