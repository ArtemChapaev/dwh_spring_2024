#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mr3_product_mapper.py"""

import sys


table_type = 'product'

for line in sys.stdin:
    product_id, description = line.strip().split('\t')

    # print first `product_id` for next sort and add `type` of current table
    print("{product_id}\t{table_type}\t{description}".format(
        product_id=product_id,
        table_type=table_type,
        description=description)
    )
