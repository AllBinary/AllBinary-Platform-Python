#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.gui.swing.workers

from __future__ import annotations

from org.allbinary.gui.swing.workers.SwingWorker import SwingWorker


class JListSwingWorker(SwingWorker):

    def _init_fields(self) -> None:
        self.jList: JList = None
        self.listModel: ListModel = None
    

    def __init__(self, jList: JList, listModel: ListModel) -> None:
        super().__init__()
        self._init_fields()
        self.setJList(jList)
        self.setListModel(listModel)
    

    def doInBackground(self) -> object:
        return None
    

    def done(self) -> None:
        self.getJList().setModel(self.getListModel())
    

    def getJList(self) -> JList:
        return self.jList
    

    def setJList(self, jList: JList) -> None:
        self.jList = jList
    

    def getListModel(self) -> ListModel:
        return self.listModel
    

    def setListModel(self, listModel: ListModel) -> None:
        self.listModel = listModel
# from javax.swing import *


