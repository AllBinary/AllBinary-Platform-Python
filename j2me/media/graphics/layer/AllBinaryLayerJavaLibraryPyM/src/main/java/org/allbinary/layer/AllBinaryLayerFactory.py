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
# package org.allbinary.layer

from __future__ import annotations

from org.allbinary.layer.AllBinaryLayerFactoryInterface import AllBinaryLayerFactoryInterface


class AllBinaryLayerFactory(AllBinaryLayerFactoryInterface):

    def _init_fields(self) -> None:
        self.rectangle: Rectangle = None
    

    def __init__(self, rectangle: Rectangle) -> None:
        self._init_fields()
        self.rectangle = rectangle
    

    def getInstance(self) -> AllBinaryLayer:
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        return AllBinaryLayer(StringUtil.getInstance().EMPTY_STRING, self.rectangle, ViewPosition.getInstanceD())
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.view.ViewPosition import ViewPosition


