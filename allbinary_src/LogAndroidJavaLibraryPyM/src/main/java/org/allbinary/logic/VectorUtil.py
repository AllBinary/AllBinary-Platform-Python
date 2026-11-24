# 
# AllBinary Open License Version 1 
# Copyright (c) 2026 AllBinary 
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
# package org.allbinary.logic

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class VectorUtil:
    instance: VectorUtil = None
    

    @staticmethod
    def getInstance() -> VectorUtil:
        return VectorUtil.instance
    

    def getSize(self, anyType: object) -> int:
        from java.util.Vector import Vector
        vector: Vector[object] = anyType
        return vector.size()
    

    def elementAt(self, anyType: object, index: int) -> object:
        from java.util.Vector import Vector
        vector: Vector[object] = anyType
        return vector.elementAt(index)
# from java.util.Vector import Vector


def _VectorUtil_instance() -> object:
    return VectorUtil()

lazy_static(VectorUtil, "instance", _VectorUtil_instance)

