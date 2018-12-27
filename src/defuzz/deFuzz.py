# -*- coding: utf-8 -*-
# Copyright: (C) 2018-2019 Lovac42
# Support: https://github.com/lovac42/DeFuzz
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.3


from aqt import mw
from anki.hooks import wrap
from anki.sched import Scheduler
from .menuopt import *
from .const import *


def fuzzIvlRange(sched, ivl, _old):
    card = mw.reviewer.card
    if not card:
        return _old(sched, ivl)
    conf=sched.col.decks.confForDid(card.odid or card.did)
    if not conf.get('defuzz',0):
        return _old(sched, ivl)
    # print('using defuzz')
    return deFuzzer(ivl, conf)


def deFuzzer(ivl, conf):
    p=m=0
    for L in FUZZ_LEVELS:
        if not L[0] or ivl < L[0]:
            m=conf.get('%s%dm'%(KEY,L[0]),L[1])
            p=conf.get(KEY+str(L[0]),L[2])
            break
    if not p:
        return [ivl, ivl]
    if ivl<=2:
        return [m, p] #possible zero
    fuzz = max(m, int(ivl*p/100.0))
    fuzz_min = max(1,ivl-fuzz)
    return [fuzz_min, ivl+fuzz]


Scheduler._fuzzIvlRange = wrap(Scheduler._fuzzIvlRange, fuzzIvlRange, 'around')
if ANKI21:
    from anki.schedv2 import Scheduler as Scheduler2
    Scheduler2._fuzzIvlRange = wrap(Scheduler2._fuzzIvlRange, fuzzIvlRange, 'around')

