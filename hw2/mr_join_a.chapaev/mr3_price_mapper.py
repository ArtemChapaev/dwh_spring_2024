#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mr3_price_mapper.py"""

import sys


table_type = 'price'

for line in sys.stdin:
    product_id, price = line.strip().split(';')

    # print first `product_id` for next sort and add `type` of current table
    print("{product_id}\t{table_type}\t{price}".format(
        product_id=product_id,
        table_type=table_type,
        price=price)
    )
