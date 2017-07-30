# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class PriceIncorrectException(Exception):
    pass


class TitleIncorrectException(Exception):
    pass


class Price(object):
    __price = None

    def __init__(self, price):
        self.__set_price(price=price)

    def __set_price(self, price):
        if price <= 0:
            raise PriceIncorrectException

        self.__price = price

    def price(self):
        return self.__price

    def __repr__(self):
        return self.__price


class Title(object):
    __title = None

    def __init__(self, title):
        self.__set_title(title=title)

    def __set_title(self, title):
        if not title or not len(title):
            raise TitleIncorrectException

        self.__title = title

    def title(self):
        return self.__title

    def __repr__(self):
        return self.__title
