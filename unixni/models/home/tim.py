from django.db import models

class Tim(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    line = models.CharField(max_length=255)
    profil = models.ImageField(upload_to='tim/')
    title2 = models.CharField(max_length=255)
    subtitle2 = models.CharField(max_length=255)
    subtitle3 = models.CharField(max_length=255)
    title3 = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Value(models.Model):
    list = models.CharField(max_length=255)

    def __str__(self):
        return self.list
    
class Pencapaian(models.Model):
    list = models.CharField(max_length=255)

    def __str__(self):
        return self.list
    
class Target(models.Model):
    list = models.CharField(max_length=255)

    def __str__(self):
        return self.list