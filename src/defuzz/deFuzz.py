# -*- coding: utf-8 -*-
# Copyright: (C) 2018-2019 Lovac42
# Support: https://github.com/lovac42/DeFuzz
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.2


from aqt import mw
from anki.hooks import wrap
from anki.sched import Scheduler
from .menuopt import *
from .const import *


def deFuzzer(sched, ivl, _old):
    card = mw.reviewer.card
    if not card:
        return _old(sched, ivl)
    conf=sched.col.decks.confForDid(card.odid or card.did)
    if not conf.get('defuzz',0):
        return _old(sched, ivl)
    # print('using defuzz')

    n=m=0
    if ivl < 2:
        return [1, 1]
    elif ivl == 2:
        n=conf.get('defuzz_ivl2',3)
        return [ivl, n]
    elif ivl < 7:
        n=conf.get('defuzz_ivl7',25)
        m=1
    elif ivl < 21:
        n=conf.get('defuzz_ivl21',15)
        m=conf.get('defuzz_ivl21m',2)
    elif ivl < 30:
        n=conf.get('defuzz_ivl30',15)
        m=conf.get('defuzz_ivl30m',2)
    elif ivl < 60:
        n=conf.get('defuzz_ivl60',5)
        m=conf.get('defuzz_ivl60m',4)
    elif ivl < 90:
        n=conf.get('defuzz_ivl90',5)
        m=conf.get('defuzz_ivl90m',4)
    elif ivl < 120:
        n=conf.get('defuzz_ivl120',5)
        m=conf.get('defuzz_ivl120m',4)
    elif ivl < 200:
        n=conf.get('defuzz_ivl200',5)
        m=conf.get('defuzz_ivl200m',4)
    else:
        n=conf.get('defuzz_ivlAll',5)
        m=conf.get('defuzz_ivlAll',4)

    if not n:
        return [ivl, ivl]
    fuzz = max(m, int(ivl*n/100.0))
    fuzz_min = max(1,ivl-fuzz)
    return [fuzz_min, ivl+fuzz]


Scheduler._fuzzIvlRange = wrap(Scheduler._fuzzIvlRange, deFuzzer, 'around')
if ANKI21:
    from anki.schedv2 import Scheduler as Scheduler2
    Scheduler2._fuzzIvlRange = wrap(Scheduler2._fuzzIvlRange, deFuzzer, 'around')

