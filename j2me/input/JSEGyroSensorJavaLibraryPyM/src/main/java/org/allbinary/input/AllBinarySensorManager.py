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
# package org.allbinary.input

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class AllBinarySensorManager:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.ORIENTATION_SENSOR_INPUT: str = "Orientation Sensor Input"
        self.ORIENTATION_TYPE: str = "Orientation Type"
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> AllBinarySensorManager:
        if AllBinarySensorManager.instance == NullUtil.getInstance().NULL_OBJECT:
            AllBinarySensorManager.instance = AllBinarySensorManager()
        return AllBinarySensorManager.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self) -> None:
        pass
    

    def getSensorNamesList(self) -> BasicArrayList:
        return self.list_
    

    def shutdown(self) -> None:
        pass
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


