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
# package org.allbinary.input.automation.module

from __future__ import annotations



class DefaultListModelHelper:

    def _init_fields(self) -> None:
        self.defaultListModel: DefaultListModel = None
        self.vector: BasicArrayList = None
    

    def __init__(self) -> None:
        from org.allbinary.input.automation.module.DefaultListModel import DefaultListModel
        self._init_fields()
        self.vector = BasicArrayListD()
        self.defaultListModel = DefaultListModel()
    

    def initDefaultModelList(self) -> None:
        from org.allbinary.input.automation.module.DefaultListModel import DefaultListModel
        self.defaultListModel = DefaultListModel()
        size: int = self.vector.size()
        for index in range(0, size):
            moduleName: str = self.vector.get(index)
            self.defaultListModel.addElement(moduleName)
    

    def getListModel(self) -> ListModel:
        return self.defaultListModel
    

    def add(self, string: str) -> None:
        self.vector.add(string)
    

    def remove(self, string: str) -> None:
        self.vector.remove(string)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.swing import *
from org.allbinary.logic.StdUtil import StdUtil


