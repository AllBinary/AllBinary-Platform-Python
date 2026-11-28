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

from java.lang.JavaRuntimeStatic import lazy_static


class ScaleProperties:
    instance: ScaleProperties = None

    def _init_fields(self) -> None:
        if "scaleX" not in vars(self): self.scaleX: float = 0.0
        if "scaleY" not in vars(self): self.scaleY: float = 0.0
        if "scaleWidth" not in vars(self): self.scaleWidth: int = 0
        if "scaleHeight" not in vars(self): self.scaleHeight: int = 0
        if "shouldScale" not in vars(self): self.shouldScale: bool = False

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonLabels import CommonLabels
        return str(StringMaker().append(CommonLabels.getInstance().COLON_SEP).appendboolean(self.shouldScale).append("scaleX: ").appendfloat(self.scaleX).append("scaleY: ").appendfloat(self.scaleY).append("scaleWidth: ").appendint(self.scaleWidth).append("scaleHeight: ").appendint(self.scaleHeight))

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonLabels import CommonLabels


def _ScaleProperties_instance() -> object:
    return ScaleProperties()

lazy_static(ScaleProperties, "instance", _ScaleProperties_instance)

