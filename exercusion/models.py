from django.db import models
from .constants import *



# Create your models here.

class Execursion(models.Model):
    id = models.CharField(max_length=20, blank=True, primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    detailPageName = models.CharField(max_length=200, blank=True, null=True)
    portID = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    typology = models.CharField(choices=TYPOLOGY,  max_length=200, blank=True, null=True)
    activityLevel = models.CharField(max_length=150, blank=True, null=True)
    collectionType = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=200, blank=True, null=True)
    language = models.CharField(choices=LANGUAGE, max_length=20, blank=True, null=True)
    priceLevel = models.CharField(max_length=20, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    mealInfo = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    shortDescription = models.CharField(max_length=150, blank=True, null=True)
    longDecription =models.TextField(blank=True, null=True)
    externalContent = models.BooleanField(default=False)
    minimumAge = models.CharField(max_length=15, blank=True, null=True)
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

