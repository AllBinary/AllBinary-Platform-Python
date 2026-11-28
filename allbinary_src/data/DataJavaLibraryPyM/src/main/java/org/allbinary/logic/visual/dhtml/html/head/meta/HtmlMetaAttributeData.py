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
# package org.allbinary.logic.visual.dhtml.html.head.meta

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_equals


class HtmlMetaAttributeData:

    def _init_fields(self) -> None:
        if "id" not in vars(self): self.id: int = 0
        if "name" not in vars(self): self.name: str = None
    

    def __init__(self, id: int, value: str) -> None:
        __class__._init_fields(self)
        self.name = value
        self.id = id
    

    def equals(self, htmlMetaAttributeData: HtmlMetaAttributeData) -> bool:
        if htmlMetaAttributeData.id == self.id:
            return True
        else:
            return False

    def __eq__(self, other: object) -> bool:
        return self.equals(other)

    __hash__ = object.__hash__
    

    def toString(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.toString()


