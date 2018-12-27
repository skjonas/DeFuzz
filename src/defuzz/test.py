# -*- coding: utf-8 -*-
# Copyright: (C) 2018-2019 Lovac42
# Support: https://github.com/lovac42/DeFuzz
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.1


from aqt import mw
from .deFuzz import *


def test(n,m):
    print("graduating interval = %d"%n)
    for i in range(n,m):
        s='ivl=%d  range='%i
        s+=str(mw.col.sched._fuzzIvlRange(i))
        print(s)

mw.defuzz_test=test

# Execute in reviewer with deck options set.
# >>> mw.defuzz_test(1,15)

