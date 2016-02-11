# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python imports
from __future__ import unicode_literals

# 3rd. libraries imports

# django imports
from django.conf.urls import url
from django.views.generic import TemplateView


# project imports

# app imports
from ships.views import ShipListView

urlpatterns = [
    url(r'^', ShipListView.as_view()),
]