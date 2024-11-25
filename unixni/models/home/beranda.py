from django.db import models

class WelcomeCard(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/home/')

    def __str__(self):
        return self.title

class ValueDescription(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)
    title4 = models.CharField(max_length=100)
    subtitle = models.TextField()

    def __str__(self):
        return self.title1

class CompanyValue(models.Model):
    abbreviation = models.CharField(max_length=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.abbreviation} - {self.description}"

class TrustedBrand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='trusted_brands/')

    def __str__(self):
        return self.name
    
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nama")
    testimonial_text = models.TextField(verbose_name="Testimoni")
    image = models.ImageField(upload_to='testimonials/', verbose_name="Gambar")

    def __str__(self):
        return f"Testimoni oleh {self.name}"
    
class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name="Pertanyaan")
    answer = models.TextField(verbose_name="Jawaban")

    def __str__(self):
        return self.question