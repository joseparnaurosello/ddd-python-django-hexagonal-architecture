# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from abc import ABCMeta, abstractmethod


class ProductRepository(object):
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def find_by_id(id):
        pass

    @staticmethod
    @abstractmethod
    def persist(product):
        pass
