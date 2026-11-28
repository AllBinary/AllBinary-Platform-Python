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
# package org.allbinary.graphics.color

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


@java_inherited_overloads
class ColorChangeEvent(AllBinaryEventObject):
    def _java_defaults(self):
        vars(self).setdefault("basicColor", None)

    def _init_fields(self) -> None:
        self.basicColor: BasicColor = BasicColorFactory.getInstance().WHITE
    

    def __init__(self, anyType: object) -> None:
        __class__._java_defaults(self)
        super().__init__(anyType)
        __class__._init_fields(self)
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        self.basicColor = basicColor
    

    def getBasicColorP(self) -> BasicColor:
        return self.basicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


