# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from catalog.factories.product_factory import ProductFactory
from catalog.repositories.ProductRepositoryDjango import ProductRepositoryDjango
from catalog.use_cases import CreateProductUseCase


def TestView(request):
    html = "<html><body>Test.</body></html>"

    product_price = 100
    product_title = 'prid test'

    product_factory = ProductFactory()
    product_repository = ProductRepositoryDjango()
    product = CreateProductUseCase(product_factory=product_factory, product_repository=product_repository).execute(product_title=product_title, product_price=product_price)

    print product.title()

    return HttpResponse(html)
