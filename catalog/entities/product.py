# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class ProductPriceException(Exception):
    pass


class Product(object):
    __id = None
    __title = None
    __price = None

    def __init__(self, id, title, price):
        self.__set_id(id)
        self.__set_title(title)
        self.__set_price(price)

    def __set_id(self, id):
        self.__id = id

    def __set_title(self, title):
        self.__title = title

    def __set_price(self, price):
        self.__price = price

    def id(self):
        return self.__id

    def title(self):
        return self.__title

    def price(self):
        return self.__price
