# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python imports

# 3rd. libraries imports

# django imports
from django.contrib import admin
# from django.utils.translation import ugettext_lazy as _

# project imports

# app imports
from ships.models import Ship


class ShipAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ship, ShipAdmin)
