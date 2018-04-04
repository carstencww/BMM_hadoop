#!/usr/bin/env python
import sys
import numpy as np
me = None
cnt = 0
total = np.zeros(28*28) #hardcoded for now
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    partial_cnt, partial_cen = value.split(':')
    partial_cen = partial_cen.split(',')
    partial_cen = [float(x) for x in partial_cen]
    partial_cen = np.asarray(partial_cen)
    partial_cnt = int(partial_cnt)
    if me is None:
        me = key
        cnt += partial_cnt
        total += partial_cen
    else:
        if me == key:
            cnt += partial_cnt
            total += partial_cen
        else:
            total = total / cnt
            print(me+'\t'+",".join(str(x) for x in total))
            me = key
            cnt = partial_cnt
            total = partial_cen
total = total / cnt
print(me+'\t'+",".join(str(x) for x in total))
