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
# package org.allbinary.logic.util.cache

from __future__ import annotations



class CacheType:

    def _init_fields(self) -> None:
        if "vendor" not in vars(self): self.vendor: str = None
        if "type_" not in vars(self): self.type_: str = None
    

    def __init__(self, vendor: str, type_: str) -> None:
        __class__._init_fields(self)
        self.vendor = vendor
        self.type_ = type_
    

    def getVendor(self) -> str:
        return self.vendor
    

    def getType(self) -> str:
        return self.type_
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("CacheType: Vendor: ")
        stringBuffer.append(self.getVendor())
        stringBuffer.append(" Type: ")
        stringBuffer.append(self.getType())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.logic.string.StringMaker import StringMaker


