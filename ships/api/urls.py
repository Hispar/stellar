# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""
# python imports
from __future__ import absolute_import, unicode_literals

# django imports
from django.conf.urls import url, include

# 3rd party imports
from rest_framework import routers

# app imports
from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'ships', views.ShipViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]