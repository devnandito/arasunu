# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from cities.models import City

class Location(models.Model):
    id_ciudad = models.ForeignKey(City, on_delete=models.CASCADE)
    lon_gra = models.DecimalField(max_digits=1000, decimal_places=8, blank=True, null=True)
    lon_min = models.DecimalField(max_digits=1000, decimal_places=8, blank=True, null=True)
    lon_seg = models.FloatField(blank=True, null=True)
    lon_hem = models.CharField(max_length=1, blank=True, null=True)
    lat_gra = models.DecimalField(max_digits=1000, decimal_places=8, blank=True, null=True)
    lat_min = models.DecimalField(max_digits=1000, decimal_places=8, blank=True, null=True)
    lat_seg = models.FloatField(blank=True, null=True)
    lat_hem = models.CharField(max_length=1, blank=True, null=True)
    elev = models.DecimalField(max_digits=1000, decimal_places=8, blank=True, null=True)
    lon_dec = models.FloatField(blank=True, null=True)
    lat_dec = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "%s" %(self.lon_seg)


    class Meta:
        verbose_name = 'Ubicación Estación'
        verbose_name_plural = 'Ubicaciones Estaciones'
        ordering = ('id',)