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

from java.lang.JavaRuntimeStatic import lazy_static


#ArkTs does not have this.  So this is for the ArkTs build.
class EnumerationUtil:
    instance: EnumerationUtil = None
    

    @staticmethod
    def getInstance() -> EnumerationUtil:
        from jsinterop.annotations.JsMethod import JsMethod
        return EnumerationUtil.instance
    

    def hasMoreElements(self, enumeration: Enumeration) -> bool:
        from java.util.Enumeration import Enumeration
        from jsinterop.annotations.JsMethod import JsMethod
        return enumeration.hasMoreElements()
    

    def nextElement(self, enumeration: Enumeration) -> object:
        from java.util.Enumeration import Enumeration
        from jsinterop.annotations.JsMethod import JsMethod
        return enumeration.nextElement()
    

    def getAsArray(self, enumeration: Enumeration) -> list[object]:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from java.util.Enumeration import Enumeration
        from jsinterop.annotations.JsMethod import JsMethod
        basicArrayList: BasicArrayList = BasicArrayListD()
        while self.hasMoreElements(enumeration):
            basicArrayList.add(self.nextElement(enumeration))
        return basicArrayList.toArray()
# from jsinterop.annotations.JsType import JsType
# from java.util.Enumeration import Enumeration
# from jsinterop.annotations.JsMethod import JsMethod


def _EnumerationUtil_instance() -> object:
    return EnumerationUtil()

lazy_static(EnumerationUtil, "instance", _EnumerationUtil_instance)

