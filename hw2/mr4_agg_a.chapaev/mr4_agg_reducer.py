#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mr4_agg_reducer.py"""

import sys


last_mark = None
general_lines_count = 0
general_count = 0

acc = []

for line in sys.stdin:
    mark, lines_count, count = line.strip().split('\t')

    # bcs lines are sorted by `mark`, we can calculate count of marks using `general_lines_count` and `general_count`
    if mark != last_mark:
        # solving problem with first `last_mark = None`
        if last_mark:
            acc.append([last_mark, general_lines_count, general_count])

        general_count = general_lines_count = 0
        last_mark = mark

    general_lines_count += int(lines_count)
    general_count += int(count)

# don't forget about last read `mark`
if last_mark:
    acc.append([last_mark, general_lines_count, general_count])

acc.sort(key=lambda x: x[2], reverse=True)
for mark, lines_count, count in acc:
    print("{punctuation_mark}:{lines_count}:{count}".format(punctuation_mark=mark, lines_count=lines_count, count=count))
