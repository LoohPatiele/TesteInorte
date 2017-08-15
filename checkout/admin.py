# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import CartItem, Order, OrderItem


admin.site.register([CartItem, Order, OrderItem])
