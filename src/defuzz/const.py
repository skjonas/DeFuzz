# -*- coding: utf-8 -*-
# Copyright: (C) 2018-2019 Lovac42
# Support: https://github.com/lovac42/DeFuzz
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.3


from anki import version
ANKI21 = version.startswith("2.1.")

KEY='defuzz_ivl'


FUZZ_LEVELS = (
    (2,1,1),   # <2, Level 1, min 1, max 1, DO NOT MOD
    (3,2,3),   # =2, Level 2, min 2, max 3, DO NOT MOD

# == User Config =========================================

# Add and remove lines as needed,

# ( Level, fuzz_min, percent )
    (   7, 1, 25 ),  # <7, IVL 1-6, min 1, 25%
    (  14, 2, 15 ),
    (  21, 2, 15 ),  # <21, IVL 1-20, min 2, 15%
    (  30, 2, 15 ),
    (  45, 4,  5 ),
    (  60, 4,  5 ),
    (  90, 4,  5 ),  # <90, IVL 1-89, min 4, 5%
    ( 120, 4,  5 ),
    ( 150, 4,  5 ),
    ( 180, 4,  5 ),
    ( 210, 4,  5 ),

# == End Config ==========================================
##########################################################

    (0,4,5)    #ALL ELSE, DO NOT MOD
)



