# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python imports
from __future__ import absolute_import, unicode_literals

# 3rd. libraries imports

# django imports
from django.views.generic import ListView


# project imports

# app imports
from ships.models import Ship


class ShipListView(ListView):
    template_name = "list.html"
    model = Ship



