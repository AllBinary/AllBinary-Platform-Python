# 
# AllBinary Open License Version 1 
# Copyright (c) 2007 AllBinary 
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
# package org.allbinary.input.motion.button

from __future__ import annotations

from org.allbinary.input.motion.button.BaseTouchInput import BaseTouchInput


class TouchButtonsListBuilder(BaseTouchInput):

    def _init_fields(self) -> None:
        self.baseTouchInputList: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def addList(self, list_: BasicArrayList) -> None:
        size: int = self.baseTouchInputList.size()
        baseTouchInput: BaseTouchInput = None
        for index in range(0, size):
            baseTouchInput = self.baseTouchInputList.get(index)
            list_.addAllList(baseTouchInput.getList())
    

    def add(self, baseTouchInput: BaseTouchInput) -> None:
        self.baseTouchInputList.add(baseTouchInput)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


