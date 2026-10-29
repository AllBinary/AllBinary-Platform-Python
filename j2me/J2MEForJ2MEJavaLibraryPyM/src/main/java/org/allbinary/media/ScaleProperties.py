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
# package org.allbinary.media

from __future__ import annotations



class ScaleProperties:
    instance: ScaleProperties = None

    def _init_fields(self) -> None:
        self.scaleX: float = 1.0
        self.scaleY: float = 1.0
        self.scaleWidth: int = 0
        self.scaleHeight: int = 0
        self.shouldScale: bool = False

    def __init__(self) -> None:
        self._init_fields()
    

    def toString(self) -> str:
        return str(StringMaker().append(CommonLabels.getInstance().COLON_SEP).appendboolean(self.shouldScale).append("scaleX: ").appendfloat(self.scaleX).append("scaleY: ").appendfloat(self.scaleY).append("scaleWidth: ").appendint(self.scaleWidth).append("scaleHeight: ").appendint(self.scaleHeight))

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels


ScaleProperties.instance = ScaleProperties()

