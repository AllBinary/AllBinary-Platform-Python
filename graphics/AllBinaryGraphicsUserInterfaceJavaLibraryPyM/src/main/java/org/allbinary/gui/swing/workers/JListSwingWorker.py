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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
# from javax.swing.SwingWorker import SwingWorker


@java_inherited_overloads
class JListSwingWorker(SwingWorker):
    def _java_defaults(self):
        vars(self).setdefault("jList", None)
        vars(self).setdefault("listModel", None)

    def _init_fields(self) -> None:
        if "jList" not in vars(self): self.jList: JList = None
        if "listModel" not in vars(self): self.listModel: ListModel = None
    

    def __init__(self, jList: JList, listModel: ListModel) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
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
# from javax.swing.JList import JList
# from javax.swing.ListModel import ListModel


