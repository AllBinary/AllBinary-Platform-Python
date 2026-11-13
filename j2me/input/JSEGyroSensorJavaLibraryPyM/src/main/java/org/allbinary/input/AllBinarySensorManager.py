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

from java.lang.JavaRuntimeStatic import lazy_static


class AllBinarySensorManager:
    instance: object = None

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.ORIENTATION_SENSOR_INPUT: str = "Orientation Sensor Input"
        self.ORIENTATION_TYPE: str = "Orientation Type"
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> AllBinarySensorManager:
        from org.allbinary.logic.NullUtil import NullUtil
        if AllBinarySensorManager.instance == NullUtil.getInstance().NULL_OBJECT:
            AllBinarySensorManager.instance = AllBinarySensorManager()
        return AllBinarySensorManager.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self) -> None:
        pass
    

    def getSensorNamesList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.list_
    

    def shutdown(self) -> None:
        pass
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


def _AllBinarySensorManager_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(AllBinarySensorManager, "instance", _AllBinarySensorManager_instance)

