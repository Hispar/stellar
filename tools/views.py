# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python imports
from __future__ import unicode_literals

# 3rd. libraries imports

# django imports
from django.contrib.auth.decorators import login_required


# project imports

# app imports


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
