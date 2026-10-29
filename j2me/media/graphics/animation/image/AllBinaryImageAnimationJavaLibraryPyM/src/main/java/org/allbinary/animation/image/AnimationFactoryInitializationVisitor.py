# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.animation.image

from __future__ import annotations



class AnimationFactoryInitializationVisitor:

    def _init_fields(self) -> None:
        self.width: int = 0
        self.height: int = 0
        self.dx: int = 0
        self.dy: int = 0
        self.originalDx: int = 0
        self.originalDy: int = 0

    def __init__(self) -> None:
        self._init_fields()
    

    def visit(self) -> None:
        pass
    

    def toString(self) -> str:
        commonSeps: CommonSeps = CommonSeps.getInstance()
        commonLabels: CommonLabels = CommonLabels.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(PositionStrings.getInstance().DX_LABEL).appendfloat(float(self.dx))
        stringBuffer.append(PositionStrings.getInstance().DY_LABEL).appendfloat(float(self.dy))
        stringBuffer.append(commonLabels.WIDTH_LABEL)
        stringBuffer.appendint(self.width)
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(commonLabels.HEIGHT_LABEL)
        stringBuffer.appendint(self.height)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.math.PositionStrings import PositionStrings
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps


