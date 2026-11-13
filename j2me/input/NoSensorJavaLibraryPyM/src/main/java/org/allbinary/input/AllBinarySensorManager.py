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
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
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
        from org.allbinary.input.accelerometer.AccelerometerSensorFactory import AccelerometerSensorFactory
        from org.allbinary.input.gyro.GyroSensorFactory import GyroSensorFactory
        self._init_fields()
        try:
            GyroSensorFactory.init()
            AccelerometerSensorFactory.init()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
    

    def init(self) -> None:
        pass
    

    def getSensorNamesList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.list_
    

    def shutdown(self) -> None:
        pass
# from org.allbinary.input.accelerometer.AccelerometerSensorFactory import AccelerometerSensorFactory
# from org.allbinary.input.gyro.GyroSensorFactory import GyroSensorFactory
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


def _AllBinarySensorManager_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(AllBinarySensorManager, "instance", _AllBinarySensorManager_instance)

