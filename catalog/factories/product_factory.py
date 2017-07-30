# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from catalog.value_objects import Price, Title
from catalog.entities.product import Product


class ProductFactory(object):
    def buid(self, title, price, id=None):
        if not id:
            id = uuid.uuid4()

        price = Price(price)
        title = Title(title)

        return Product(id=id, title=title, price=price)
