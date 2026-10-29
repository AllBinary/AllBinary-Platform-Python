# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.logic.util.visitor.Visitor import Visitor


class SteeringVisitor(Visitor):

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def getList(self) -> BasicArrayList:
        return self.list_
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


