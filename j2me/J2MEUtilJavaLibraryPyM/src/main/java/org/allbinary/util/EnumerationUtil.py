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
# package org.allbinary.util

from __future__ import annotations



#ArkTs does not have this.  So this is for the ArkTs build.
class EnumerationUtil:
    instance: EnumerationUtil = None
    

    @staticmethod
    def getInstance() -> EnumerationUtil:
        return EnumerationUtil.instance
    

    def hasMoreElements(self, enumeration: Enumeration) -> bool:
        return enumeration.hasMoreElements()
    

    def nextElement(self, enumeration: Enumeration) -> object:
        return enumeration.nextElement()
    

    def getAsArray(self, enumeration: Enumeration) -> list[object]:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        basicArrayList: BasicArrayList = BasicArrayListD()
        while self.hasMoreElements(enumeration):
            basicArrayList.add(self.nextElement(enumeration))
        return basicArrayList.toArray()
from jsinterop.annotations.JsType import JsType
# from java.util.Enumeration import Enumeration
from jsinterop.annotations.JsMethod import JsMethod


EnumerationUtil.instance = EnumerationUtil()

