from django.db import models
from .constants import *



# Create your models here.

class Execursion(models.Model):
    id = models.CharField(max_length=20, blank=True, primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    detailPageName = models.CharField(max_length=200, blank=True)
    portID = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=50, blank=True)
    typology = models.CharField(choices=TYPOLOGY,  max_length=200, blank=True)
    activityLevel = models.CharField(max_length=150, blank=True)
    collectionType = models.CharField(max_length=100, blank=True)
    duration = models.CharField(max_length=200, blank=True)
    language = models.CharField(choices=LANGUAGE, max_length=20, blank=True)
    priceLevel = models.CharField(max_length=20, blank=True)
    currency = models.CharField(max_length=10, blank=True)
    mealInfo = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=15, blank=True)
    shortDescription = models.CharField(max_length=150, blank=True)
    longDecription =models.TextField(blank=True)
    externalContent = models.BooleanField(default=False)
    minimumAge = models.CharField(max_length=15, blank=True)
    wheelChairAccessible = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("execursion:execursion_detail", args=[self.id])
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Execursion'
        verbose_name_plural = 'Execursions'

