# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class CreateProductUseCase(object):
    __product_factory = None
    __product_repository = None

    def __init__(self, product_factory, product_repository):
        self.__set_product_factory(product_factory=product_factory)
        self.__set_product_repository(product_repository=product_repository)

    def __set_product_factory(self, product_factory):
        self.__product_factory = product_factory

    def __set_product_repository(self, product_repository):
        self.__product_repository = product_repository

    def execute(self, product_title, product_price):
        product = self.__product_factory.buid(title=product_title, price=product_price)
        self.__product_repository.persist(product=product)

        return product
