from django.db import models


# Create your models here.

class Strains(models.Model):
    strain_name = models.CharField(max_length=20, blank=False, null=False)
    thc = models.IntegerField()
    effect = models.CharField(max_length=50, blank=False, null=False)
    cost_blunt = models.IntegerField()
    product_image = models.ImageField(upload_to="strains/", blank=True, null=True)

    def __str__(self):
        return self.strain_name


class Sliders(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sliders', default='profile.png')

    def __str__(self):
        return self.heading


class Mainpage(models.Model):
    heading = models.CharField(max_length=100)
    btn = models.CharField(max_length=100)
    image = models.ImageField(upload_to='homepage', default='profile.png')

    def __str__(self):
        return self.heading
