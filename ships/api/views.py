# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""
# python imports
from __future__ import absolute_import, unicode_literals

# third party imports
from rest_framework import viewsets

# django imports

# app imports
from ships.models import Ship
from .serializers import ShipSerializer


class ShipViewSet(viewsets.ModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer
