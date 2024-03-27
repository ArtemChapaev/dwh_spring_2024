#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mr3_join_reducer.py"""

import sys


last_product_id = None
product_descriptions = []
product_prices = []

for line in sys.stdin:
    product_id, table_type, data = line.strip().split('\t')

    # bcs lines are sorted by `product_id` we can JOIN lines when product_id was changed
    if product_id != last_product_id:
        # solving problem with first `last_product_id = None`
        if last_product_id:
            for descr in product_descriptions:
                for price in product_prices:
                    print("{product_id}\t{descr}\t{price}".format(product_id=last_product_id, descr=descr, price=price))

        last_product_id = product_id
        product_descriptions = []
        product_prices = []

    # in dependence of `table_type` choose array for next correct JOIN
    if table_type == 'product':
        product_descriptions.append(data)
    elif table_type == 'price':
        product_prices.append(data)


# don't forget about last read `product_id`
if last_product_id:
    for descr in product_descriptions:
        for price in product_prices:
            print("{product_id}\t{descr}\t{price}".format(product_id=last_product_id, descr=descr, price=price))
