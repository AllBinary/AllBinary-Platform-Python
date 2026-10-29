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
# package org.allbinary.logic.system.hardware.android

from __future__ import annotations

from org.allbinary.logic.system.hardware.HardwareInterface import HardwareInterface


class AndroidHardware(HardwareInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.componentInterfaceVector: BasicArrayList = BasicArrayListD()
        self.PROC_BUS_INPUT_DIRECTORY: str = "/proc/bus/input/"
        self.DEVICES: str = self.PROC_BUS_INPUT_DIRECTORY + "devices/"
        self.MINHARDWARE: int = 3
    

    def __init__(self) -> None:
        self._init_fields()
        self.init(self.DEVICES)
        size: int = self.componentInterfaceVector.size()
        if size < self.MINHARDWARE:
            raise Exception("Not Enough Data For A Valid License On Linux")
    

    # throws Exception
    def init(self, filePath: str) -> None:
        lineNumberReader: Closeable = NullCloseable.NULL_CLOSEABLE
        try:
            lineNumberReader = self.get(filePath)
        except Exception as e:
            self.logUtil.put("Hardware Data: " + str(self), self, self.commonStrings.INIT, e)
            raise e
        finally:
            if lineNumberReader is not None:
                lineNumberReader.close()
    

    # throws Exception
    def get(self, filePath: str) -> LineNumberReader:
        self.componentInterfaceVector = BasicArrayListD()
        pciFile: FileReader = FileReader(filePath)
        lineNumberReader: LineNumberReader = LineNumberReader(pciFile)
        self.logUtil.putF("File Found", self, self.commonStrings.CONSTRUCTOR)
        nextLine: str = lineNumberReader.readLine()
        while nextLine is not None:
            nextLine = lineNumberReader.readLine()
            self.componentInterfaceVector.add(UnknownHardware(nextLine))
        return lineNumberReader
    

    def getComponent(self, index: int) -> HardwareComponentInterface:
        return self.componentInterfaceVector.get(index)
    

    def toString(self) -> str:
        stringBuilder: StringMaker = StringMaker()
        size: int = self.componentInterfaceVector.size()
        for index in range(0, size):
            componentInterface: HardwareComponentInterface = self.componentInterfaceVector.get(index)
            stringBuilder.append(str(componentInterface))
            stringBuilder.append(CommonSeps.getInstance().NEW_LINE)
        return str(stringBuilder)

    def __str__(self) -> str:
        return self.toString()
    

    def compareTo(self, hardwareInterface: HardwareInterface) -> bool:
        return True
    

    def difference(self, hardwareInterface: HardwareInterface) -> ABHashtable[object, object]:
        return StdUtil.getInstance().NULL_TABLE
# from java.io.Closeable import Closeable
# from java.io.FileReader import FileReader
# from java.io.LineNumberReader import LineNumberReader
from org.allbinary.logic.io.NullCloseable import NullCloseable
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.hardware.components.android.UnknownHardware import UnknownHardware
from org.allbinary.logic.system.hardware.components.interfaces.HardwareComponentInterface import HardwareComponentInterface
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


