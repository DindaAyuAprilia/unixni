from django.db import models

class About(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    line = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='about/')
    description = models.TextField()
    title2 = models.CharField(max_length=255)
    subtitle2 = models.CharField(max_length=255)
    description2 = models.TextField()
    subtitle3 = models.CharField(max_length=255)
    description3 = models.TextField()
    title3 = models.CharField(max_length=255)
    description4 = models.TextField()
    title4 = models.CharField(max_length=255)
    description5 = models.TextField()
    title5 = models.CharField(max_length=255)
    diagram = models.ImageField(upload_to='about/')
    title6 = models.CharField(max_length=255)
    description6 = models.TextField()
    title7 = models.CharField(max_length=255)
    description7 = models.TextField()

    def __str__(self):
        return self.title

class Mission(models.Model):
    list = models.CharField(max_length=255)

    def __str__(self):
        return self.list
    
class Structur(models.Model):
    list = models.CharField(max_length=255)

    def __str__(self):
        return self.list