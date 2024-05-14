#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mapper.py"""

import sys

for line in sys.stdin:
    partner_id, show_type, user_id, cost, fraud = line.strip().split(',')
    if fraud != 'true':
        print('{partner_id}\t{cost}'.format(partner_id=partner_id, cost=cost))


# mapred streaming \
# -D mapred.reduce.tasks=1 \
# -input /hdfs/path/to/data \
# -output data/result \
# -mapper mapper.py \
# -reducer reducer.py \
# -file mapper.py \
# -file reducer.py
