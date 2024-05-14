#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""reducer.py"""

import sys

min_partner_id = None
min_partner_cost = 0

prev_partner_id = None
current_partner_cost = 0

for line in sys.stdin:
    partner_id, cost = line.strip().split('\t')

    if partner_id != prev_partner_id:
        if min_partner_id is None or current_partner_cost < min_partner_cost:
            min_partner_id = prev_partner_id
            min_partner_cost = current_partner_cost

        current_partner_cost = 0
        prev_partner_id = partner_id

    current_partner_cost += float(cost)

if min_partner_id is None or current_partner_cost < min_partner_cost:
    min_partner_id = prev_partner_id
    min_partner_cost = current_partner_cost

print("{partner_id}:{payout}".format(partner_id=min_partner_id, payout=min_partner_cost))
