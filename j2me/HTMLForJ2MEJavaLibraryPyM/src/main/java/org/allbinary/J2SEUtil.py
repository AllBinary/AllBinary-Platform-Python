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
# package org.allbinary

from __future__ import annotations



#HTMLForJ2ME
class J2SEUtil:
    instance: J2SEUtil = None
    

    @staticmethod
    def getInstance() -> J2SEUtil:
        return J2SEUtil.instance
    

    def getHashMapAsArray(self, hashMap: dict) -> list[object]:
        objectArray: list[object] = hashMap.keySet().toArray()
        return objectArray
    

    def getMapAsArray(self, map: Map[object, object]) -> list[object]:
        objectArray: list[object] = map.keySet().toArray()
        return objectArray
    

    def getSetAsArray(self, set: Set[str]) -> list[object]:
        objectArray: list[object] = set.toArray()
        return objectArray
# from java.util.HashMap import HashMap
# from java.util.Map import Map
# from java.util.Set import Set


J2SEUtil.instance = J2SEUtil()

