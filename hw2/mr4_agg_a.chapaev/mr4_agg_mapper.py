#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mr4_agg_mapper.py"""

import sys
from collections import Counter


marks = '.,?;:!-"\'()[]{}<>'

for line in sys.stdin:
    counter = Counter(line.strip())

    for mark in marks:
        count = counter[mark]
        if count:
            print("{mark}\t{lines_count}\t{count}".format(mark=mark, lines_count=1, count=count))
