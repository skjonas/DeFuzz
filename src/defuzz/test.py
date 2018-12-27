# -*- coding: utf-8 -*-
# Copyright: (C) 2018-2019 Lovac42
# Support: https://github.com/lovac42/DeFuzz
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.2


from aqt import mw
from aqt.utils import showInfo
from .deFuzz import *


def test_state():
    if mw.state!='review':
        print('This must be run in the Reviewer')
        return False
    card=mw.reviewer.card
    conf=mw.col.decks.confForDid(card.odid or card.did)
    if not conf.get('defuzz',0):
        print('DeFuzz is off, using anki default fuzz range.\n')
    else:
        print('DeFuzz is on.\n')
    return True


def test_ivl(n,m):
    if not test_state(): return
    print("Graduating interval = %d"%n)
    for i in range(n,m):
        s='ivl=%2d  range='%i
        s+=str(mw.col.sched._fuzzIvlRange(i))
        print(s)


# Execute in reviewer with deck options set.
# >>> mw.defuzz_test( graduating_ivl, range )
mw.defuzz_test=test_ivl
