# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""
# python imports
from __future__ import absolute_import, unicode_literals
# django imports

# 3rd party imports
from rest_framework import serializers

# app imports
from ships.models import Ship


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ('id', 'name', 'image', 'description', 'fabrication_date', 'hp', 'power', 'color', 'detection',
                  'boost', 'passengers')
