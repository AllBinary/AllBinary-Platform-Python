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
# package org.allbinary.input.media.image

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class InputImageType:
    hashMap: HashMap = None
    TYPE_VECTOR: BasicArrayList = None
    CAPTURE: InputImageType = None
    COMPARISON: InputImageType = None
    MOTION: InputImageType = None

    def _init_fields(self) -> None:
        self.name: str = None
        self.index: int = None
    

    def __init__(self, name: str, index: int) -> None:
        self._init_fields()
        self.name = name
        self.index = index
        InputImageType.TYPE_VECTOR.add(self)
        InputImageType.hashMap.put(self.getName(), self)
    

    def toString(self) -> str:
        return "ImageType: " + self.getName()

    def __str__(self) -> str:
        return self.toString()
    

    def getName(self) -> str:
        return self.name
    

    @staticmethod
    def getInstance(imageTypeString: str) -> InputImageType:
        return InputImageType.hashMap.get(imageTypeString)
    

    @staticmethod
    def getAllAsVector() -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return InputImageType.TYPE_VECTOR
    

    def getIndex(self) -> int:
        return self.index
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.StdUtil import StdUtil


def _InputImageType_hashMap() -> object:
    from java.util.HashMap import HashMap
    from org.allbinary.logic.StdUtil import StdUtil
    return StdUtil.getInstance().createHashMap()

lazy_static(InputImageType, "hashMap", _InputImageType_hashMap)

def _InputImageType_TYPE_VECTOR() -> object:
    from org.allbinary.util.BasicArrayList import BasicArrayList
    from org.allbinary.util.BasicArrayListD import BasicArrayListD
    return BasicArrayListD()

lazy_static(InputImageType, "TYPE_VECTOR", _InputImageType_TYPE_VECTOR)

def _InputImageType_CAPTURE() -> object:
    return InputImageType("Capture", 0)

lazy_static(InputImageType, "CAPTURE", _InputImageType_CAPTURE)

def _InputImageType_COMPARISON() -> object:
    return InputImageType("Comparison", 1)

lazy_static(InputImageType, "COMPARISON", _InputImageType_COMPARISON)

def _InputImageType_MOTION() -> object:
    return InputImageType("Motion", 2)

lazy_static(InputImageType, "MOTION", _InputImageType_MOTION)

