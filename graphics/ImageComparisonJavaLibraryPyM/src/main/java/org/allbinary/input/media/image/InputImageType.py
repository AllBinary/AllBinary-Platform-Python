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

from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil


class InputImageType:
    hashMap: dict = StdUtil.getInstance().createHashMap()
    TYPE_VECTOR: BasicArrayList = BasicArrayListD()
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
        return InputImageType.TYPE_VECTOR
    

    def getIndex(self) -> int:
        return self.index
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList


InputImageType.CAPTURE = InputImageType("Capture", 0)

InputImageType.COMPARISON = InputImageType("Comparison", 1)

InputImageType.MOTION = InputImageType("Motion", 2)

