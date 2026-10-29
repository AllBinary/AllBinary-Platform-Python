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
# package org.allbinary.logic.util.cache

from __future__ import annotations



class ImageCacheable:

    def _init_fields(self) -> None:
        self.name: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self, name: str, anyType: object) -> None:
        self._init_fields()
    

    def getKey(self) -> object:
        return self.name
    

    def toString(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringUtil import StringUtil


