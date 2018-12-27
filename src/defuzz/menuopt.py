# -*- coding: utf-8 -*-
# Copyright: (C) 2018-2019 Lovac42
# Support: https://github.com/lovac42/DeFuzz
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.1


import aqt
import aqt.deckconf
from aqt import mw
from anki.hooks import wrap
from .const import *

if ANKI21:
    from PyQt5 import QtCore, QtGui, QtWidgets
else:
    from PyQt4 import QtCore, QtGui as QtWidgets


def dconfsetupUi(self, Dialog):
    r=0
    tabDF = QtWidgets.QWidget()
    vLayoutDF = QtWidgets.QVBoxLayout(tabDF)
    layoutDF = QtWidgets.QGridLayout()

    self.defuzz = QtWidgets.QCheckBox(self.tab_3)
    self.defuzz.setText(_('Use deFuzz'))
    layoutDF.addWidget(self.defuzz, r, 0, 1, 1)
    r+=1

    lb_defuzz_ivl2 = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl2.setText(_("ivl max @ ivl=2:"))
    layoutDF.addWidget(lb_defuzz_ivl2, r, 0, 1, 1)

    self.defuzz_ivl2 = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl2.setMinimum(2)
    self.defuzz_ivl2.setMaximum(69)
    layoutDF.addWidget(self.defuzz_ivl2, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivl7 = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl7.setText(_("%fuzz @ ivl<7: (0=disable)"))
    layoutDF.addWidget(lb_defuzz_ivl7, r, 0, 1, 1)

    self.defuzz_ivl7 = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl7.setMinimum(0)
    self.defuzz_ivl7.setMaximum(666)
    layoutDF.addWidget(self.defuzz_ivl7, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivl21 = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl21.setText(_("%fuzz @ ivl<21: (0=dis)"))
    layoutDF.addWidget(lb_defuzz_ivl21, r, 0, 1, 1)

    self.defuzz_ivl21 = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl21.setMinimum(0)
    self.defuzz_ivl21.setMaximum(666)
    layoutDF.addWidget(self.defuzz_ivl21, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivl21m = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl21m.setText(_("smallest fuzz @ ivl<21:"))
    layoutDF.addWidget(lb_defuzz_ivl21m, r, 0, 1, 1)

    self.defuzz_ivl21m = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl21m.setMinimum(1)
    self.defuzz_ivl21m.setMaximum(999)
    layoutDF.addWidget(self.defuzz_ivl21m, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivl30 = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl30.setText(_("%fuzz @ ivl<30: (0=dis)"))
    layoutDF.addWidget(lb_defuzz_ivl30, r, 0, 1, 1)

    self.defuzz_ivl30 = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl30.setMinimum(0)
    self.defuzz_ivl30.setMaximum(666)
    layoutDF.addWidget(self.defuzz_ivl30, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivl30m = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl30m.setText(_("smallest fuzz @ ivl<30:"))
    layoutDF.addWidget(lb_defuzz_ivl30m, r, 0, 1, 1)

    self.defuzz_ivl30m = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl30m.setMinimum(1)
    self.defuzz_ivl30m.setMaximum(999)
    layoutDF.addWidget(self.defuzz_ivl30m, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivl60 = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl60.setText(_("%fuzz @ ivl<60: (0=dis)"))
    layoutDF.addWidget(lb_defuzz_ivl60, r, 0, 1, 1)

    self.defuzz_ivl60 = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl60.setMinimum(0)
    self.defuzz_ivl60.setMaximum(666)
    layoutDF.addWidget(self.defuzz_ivl60, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivl60m = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl60m.setText(_("smallest fuzz @ ivl<60:"))
    layoutDF.addWidget(lb_defuzz_ivl60m, r, 0, 1, 1)

    self.defuzz_ivl60m = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl60m.setMinimum(1)
    self.defuzz_ivl60m.setMaximum(999)
    layoutDF.addWidget(self.defuzz_ivl60m, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivl90 = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl90.setText(_("%fuzz @ ivl<90: (0=dis)"))
    layoutDF.addWidget(lb_defuzz_ivl90, r, 0, 1, 1)

    self.defuzz_ivl90 = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl90.setMinimum(0)
    self.defuzz_ivl90.setMaximum(666)
    layoutDF.addWidget(self.defuzz_ivl90, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivl90m = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl90m.setText(_("smallest fuzz @ ivl<90:"))
    layoutDF.addWidget(lb_defuzz_ivl90m, r, 0, 1, 1)

    self.defuzz_ivl90m = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl90m.setMinimum(1)
    self.defuzz_ivl90m.setMaximum(999)
    layoutDF.addWidget(self.defuzz_ivl90m, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivl120 = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl120.setText(_("%fuzz @ ivl<120: (0=dis)"))
    layoutDF.addWidget(lb_defuzz_ivl120, r, 0, 1, 1)

    self.defuzz_ivl120 = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl120.setMinimum(0)
    self.defuzz_ivl120.setMaximum(666)
    layoutDF.addWidget(self.defuzz_ivl120, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivl120m = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl120m.setText(_("smallest fuzz @ ivl<120:"))
    layoutDF.addWidget(lb_defuzz_ivl120m, r, 0, 1, 1)

    self.defuzz_ivl120m = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl120m.setMinimum(1)
    self.defuzz_ivl120m.setMaximum(999)
    layoutDF.addWidget(self.defuzz_ivl120m, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivl200 = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl200.setText(_("%fuzz @ ivl<200: (0=dis)"))
    layoutDF.addWidget(lb_defuzz_ivl200, r, 0, 1, 1)

    self.defuzz_ivl200 = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl200.setMinimum(0)
    self.defuzz_ivl200.setMaximum(666)
    layoutDF.addWidget(self.defuzz_ivl200, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivl200m = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivl200m.setText(_("smallest fuzz @ ivl<200:"))
    layoutDF.addWidget(lb_defuzz_ivl200m, r, 0, 1, 1)

    self.defuzz_ivl200m = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivl200m.setMinimum(1)
    self.defuzz_ivl200m.setMaximum(999)
    layoutDF.addWidget(self.defuzz_ivl200m, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivlAll = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivlAll.setText(_("% fuzz all else:"))
    layoutDF.addWidget(lb_defuzz_ivlAll, r, 0, 1, 1)

    self.defuzz_ivlAll = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivlAll.setMinimum(0)
    self.defuzz_ivlAll.setMaximum(666)
    layoutDF.addWidget(self.defuzz_ivlAll, r, 1, 1, 1)
    r+=1

    lb_defuzz_ivlAllm = QtWidgets.QLabel(tabDF)
    lb_defuzz_ivlAllm.setText(_("smallest fuzz for all else:"))
    layoutDF.addWidget(lb_defuzz_ivlAllm, r, 0, 1, 1)

    self.defuzz_ivlAllm = QtWidgets.QSpinBox(tabDF)
    self.defuzz_ivlAllm.setMinimum(1)
    self.defuzz_ivlAllm.setMaximum(999)
    layoutDF.addWidget(self.defuzz_ivlAllm, r, 1, 1, 1)
    r+=1

    vLayoutDF.addLayout(layoutDF)
    spacerItem1 = QtWidgets.QSpacerItem(20, 152, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    vLayoutDF.addItem(spacerItem1)
    self.tabWidget.addTab(tabDF, "DeFuzz")

def loadConf(self):
    cb=self.conf.get("defuzz", 0)
    self.form.defuzz.setCheckState(cb)
    n=self.conf.get("defuzz_ivl2", 3)
    self.form.defuzz_ivl2.setValue(n)
    n=self.conf.get("defuzz_ivl7", 25)
    self.form.defuzz_ivl7.setValue(n)
    n=self.conf.get("defuzz_ivl21", 15)
    self.form.defuzz_ivl21.setValue(n)
    n=self.conf.get("defuzz_ivl21m", 2)
    self.form.defuzz_ivl21m.setValue(n)
    n=self.conf.get("defuzz_ivl30", 15)
    self.form.defuzz_ivl30.setValue(n)
    n=self.conf.get("defuzz_ivl30m", 2)
    self.form.defuzz_ivl30m.setValue(n)
    n=self.conf.get("defuzz_ivl60", 5)
    self.form.defuzz_ivl60.setValue(n)
    n=self.conf.get("defuzz_ivl60m", 4)
    self.form.defuzz_ivl60m.setValue(n)
    n=self.conf.get("defuzz_ivl90", 5)
    self.form.defuzz_ivl90.setValue(n)
    n=self.conf.get("defuzz_ivl90m", 4)
    self.form.defuzz_ivl90m.setValue(n)
    n=self.conf.get("defuzz_ivl120", 5)
    self.form.defuzz_ivl120.setValue(n)
    n=self.conf.get("defuzz_ivl120m", 4)
    self.form.defuzz_ivl120m.setValue(n)
    n=self.conf.get("defuzz_ivl200", 5)
    self.form.defuzz_ivl200.setValue(n)
    n=self.conf.get("defuzz_ivl200m", 4)
    self.form.defuzz_ivl200m.setValue(n)
    n=self.conf.get("defuzz_ivlAll", 5)
    self.form.defuzz_ivlAll.setValue(n)
    n=self.conf.get("defuzz_ivlAllm", 4)
    self.form.defuzz_ivlAllm.setValue(n)

def saveConf(self):
    self.conf['defuzz']=self.form.defuzz.checkState()
    self.conf['defuzz_ivl2']=self.form.defuzz_ivl2.value()
    self.conf['defuzz_ivl7']=self.form.defuzz_ivl7.value()
    self.conf['defuzz_ivl21']=self.form.defuzz_ivl21.value()
    self.conf['defuzz_ivl30']=self.form.defuzz_ivl30.value()
    self.conf['defuzz_ivl30m']=self.form.defuzz_ivl30m.value()
    self.conf['defuzz_ivl60']=self.form.defuzz_ivl60.value()
    self.conf['defuzz_ivl60m']=self.form.defuzz_ivl60m.value()
    self.conf['defuzz_ivl90']=self.form.defuzz_ivl90.value()
    self.conf['defuzz_ivl90m']=self.form.defuzz_ivl90m.value()
    self.conf['defuzz_ivl120']=self.form.defuzz_ivl120.value()
    self.conf['defuzz_ivl120m']=self.form.defuzz_ivl120m.value()
    self.conf['defuzz_ivl200']=self.form.defuzz_ivl200.value()
    self.conf['defuzz_ivl200m']=self.form.defuzz_ivl200m.value()
    self.conf['defuzz_ivlAll']=self.form.defuzz_ivlAll.value()
    self.conf['defuzz_ivlAllm']=self.form.defuzz_ivlAllm.value()

aqt.forms.dconf.Ui_Dialog.setupUi = wrap(aqt.forms.dconf.Ui_Dialog.setupUi, dconfsetupUi, pos="after")
aqt.deckconf.DeckConf.loadConf = wrap(aqt.deckconf.DeckConf.loadConf, loadConf, pos="after")
aqt.deckconf.DeckConf.saveConf = wrap(aqt.deckconf.DeckConf.saveConf, saveConf, pos="before")
