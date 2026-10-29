# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.osgi.framework

from __future__ import annotations



class NullServiceReference:
    

    def getProperty(self, key: str) -> object:
        return NullUtil.getInstance().NULL_OBJECT
    

    def getPropertyKeys(self) -> list[str]:
        return StringUtil.getInstance().getArrayInstance()
    

    def compareTo(self, o: object) -> int:
        raise RuntimeError()
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.string.StringUtil import StringUtil


