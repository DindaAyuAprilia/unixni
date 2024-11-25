from django.db import models

class GaleriUtama(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    line = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Galeri(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class GaleriItem(models.Model):
    galeri = models.ForeignKey(Galeri, on_delete=models.CASCADE, related_name='items')
    image = models.ImageField(upload_to='galeri/')
    date = models.DateField()

    def __str__(self):
        return f"{self.galeri.title} - {self.date}"
