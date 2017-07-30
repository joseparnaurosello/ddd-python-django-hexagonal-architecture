# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from catalog.repositories.ProductRepository import ProductRepository
from catalog.models.Product import Product


class ProductDoesNotExistException(Exception):
    pass


class ProductPersistException(Exception):
    pass


class ProductRepositoryDjango(ProductRepository):
    @staticmethod
    def find_by_id(id):
        try:
            product = Product.objects.get(id=id)
        except ObjectDoesNotExist:
            raise ProductDoesNotExistException

        return product

    @staticmethod
    def persist(product):
        defaults = {
            'title': product.title(),
            'price': product.price().price(),
        }

        try:
            return Product.objects.update_or_create(
                id=product.id(),
                defaults=defaults,
            )
        except OverflowError:
            raise ProductPersistException
