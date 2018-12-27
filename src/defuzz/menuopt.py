# -*- coding: utf-8 -*-
# Copyright: (C) 2018-2019 Lovac42
# Support: https://github.com/lovac42/DeFuzz
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.2


import aqt
import aqt.deckconf
from aqt import mw
from anki.hooks import wrap
from .const import *

if ANKI21:
    from PyQt5 import QtCore, QtGui, QtWidgets
else: from PyQt4 import QtCore, QtGui as QtWidgets


def dconfsetupUi(self, Dialog):
    r=0
    tabDF = QtWidgets.QWidget()
    vLayoutDF = QtWidgets.QVBoxLayout(tabDF)
    layoutDF = QtWidgets.QGridLayout()

    self.defuzz = QtWidgets.QCheckBox(self.tab_3)
    self.defuzz.setText(_('Use deFuzz'))
    layoutDF.addWidget(self.defuzz, r, 0, 1, 1)
    r+=1

    self.defuzz_perc=[]
    self.defuzz_fuzz=[]
    for L in FUZZ_LEVELS:
        label=QtWidgets.QLabel(tabDF)
        if not L[0]:
            label.setText(_("min(n, %fuzz) @ all else: (0%=disable)"))
        elif L[0] <=3: #looks weird...
            label.setText(_("rand(min_ivl, max_ivl) @ ivl=%d:"%(L[0]-1)))
        else:
            label.setText(_("min(n, %%fuzz) @ ivl<%d: (0%%=disable)"%L[0]))
        layoutDF.addWidget(label, r, 0, 1, 1)

        mFuzz=QtWidgets.QSpinBox(tabDF)
        mFuzz.setMinimum(1)
        mFuzz.setMaximum(69)
        mFuzz.setMaximumWidth(80)
        self.defuzz_fuzz.append(mFuzz)
        layoutDF.addWidget(mFuzz, r, 1, 1, 1)

        perc=QtWidgets.QSpinBox(tabDF)
        perc.setMinimum(0)
        perc.setMaximum(666)
        perc.setMaximumWidth(120)
        self.defuzz_perc.append(perc)
        layoutDF.addWidget(perc, r, 2, 1, 1)
        r+=1

    vLayoutDF.addLayout(layoutDF)
    spacerItem1 = QtWidgets.QSpacerItem(20, 152, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    vLayoutDF.addItem(spacerItem1)
    self.tabWidget.addTab(tabDF, "DeFuzz")


def loadConf(self):
    cb=self.conf.get("defuzz", 0)
    self.form.defuzz.setCheckState(cb)
    i=0
    for L in FUZZ_LEVELS:
        n=self.conf.get('%s%d'%(KEY,L[0]),L[2])
        self.form.defuzz_perc[i].setValue(n)
        m=self.conf.get('%s%dm'%(KEY,L[0]),L[1])
        self.form.defuzz_fuzz[i].setValue(m)
        i+=1


def saveConf(self):
    self.conf['defuzz']=self.form.defuzz.checkState()
    i=0
    for L in FUZZ_LEVELS:
        self.conf['%s%d'%(KEY,L[0])]=self.form.defuzz_perc[i].value()
        self.conf['%s%dm'%(KEY,L[0])]=self.form.defuzz_fuzz[i].value()
        i+=1


aqt.forms.dconf.Ui_Dialog.setupUi = wrap(aqt.forms.dconf.Ui_Dialog.setupUi, dconfsetupUi, pos="after")
aqt.deckconf.DeckConf.loadConf = wrap(aqt.deckconf.DeckConf.loadConf, loadConf, pos="after")
aqt.deckconf.DeckConf.saveConf = wrap(aqt.deckconf.DeckConf.saveConf, saveConf, pos="before")
