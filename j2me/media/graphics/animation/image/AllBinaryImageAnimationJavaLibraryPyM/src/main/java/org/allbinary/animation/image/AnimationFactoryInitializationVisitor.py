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
        if "width" not in vars(self): self.width: int = 0
        if "height" not in vars(self): self.height: int = 0
        if "dx" not in vars(self): self.dx: int = 0
        if "dy" not in vars(self): self.dy: int = 0
        if "originalDx" not in vars(self): self.originalDx: int = 0
        if "originalDy" not in vars(self): self.originalDy: int = 0

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def visit(self) -> None:
        pass
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.math.PositionStrings import PositionStrings
        from org.allbinary.string.CommonLabels import CommonLabels
        from org.allbinary.string.CommonSeps import CommonSeps
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
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.math.PositionStrings import PositionStrings
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.string.CommonSeps import CommonSeps


