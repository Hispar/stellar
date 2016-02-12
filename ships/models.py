# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python imports
from __future__ import absolute_import, unicode_literals

# 3rd. libraries imports

# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _


# project imports
from tools.models import DateModificationModelMixin


# app imports


class Ship(DateModificationModelMixin):
    """Model to represent Ships

    Attributes:
        name: string
        image: string
        description: text
        fabrication_date: datetime
        hp: string
        power: string
        color: string
        detection: boolean
        boost: boolean
        passengers: integer
        reservation_date: datetime
        lat: float
        lon: float
    """
    name = models.CharField(
        verbose_name=_('name'),
        max_length=200)
    image = models.URLField(
        verbose_name=_('image'),
    )
    description = models.TextField(
        verbose_name=_('ship description'),
    )
    fabrication_date = models.DateTimeField(
        verbose_name=_('fabrication date'),
    )
    hp = models.CharField(
        verbose_name=_('horse power'),
        max_length=10)
    power = models.CharField(
        verbose_name=_('power'),
        max_length=5)
    color = models.CharField(
        verbose_name=_('color'),
        max_length=5)
    detection = models.BooleanField(
        verbose_name=_('enable detection'),
        default=False)
    boost = models.BooleanField(
        verbose_name=_('insterestelar turbo boost'),
        default=False)
    passengers = models.IntegerField(
        verbose_name=_('number of passengers'),
        default=3
    )
    reservation_date = models.DateTimeField(
        verbose_name=_('reservation date'),
        null=True,
        blank=True
    )
    lat = models.FloatField(
        verbose_name=_('Latitude'),
        blank=True,
        null=True
    )
    lon = models.FloatField(
        verbose_name=_('Longitude'),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id', 'name')
