from django.db import models
from .constants import *



# Create your models here.

class Execursion(models.Model):
    name = models.CharField(max_length=200)
    data_page_name = models.SlugField(max_length=200)
    port_id = models.CharField(max_length=100)
    trip_type = models.CharField(max_length=50)
    typology = models.CharField(choices=TYPOLOGY,  max_length=200)
    activity_level = models.CharField(max_length=150)
    collectionType = models.CharField(max_length=100)
    duration = models.CharField(max_length=200)
    language = models.CharField(choices=LANGUAGE, max_length=20)
    price_level = models.CharField(max_length=20)
    currency = models.CharField(max_length=10)
    meal_info = models.CharField(max_length=50)
    status = models.CharField(max_length=15)
    short_description = models.CharField(max_length=150)
    long_description =models.TextField()
    external_content = models.BooleanField(default=False)
    minimum_age = models.CharField(max_length=15)
    wheel_chair_accessible = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("execursion:execursion_detail", args=[self.id])
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Execursion'
        verbose_name_plural = 'Execursions'

