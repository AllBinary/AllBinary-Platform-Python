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
# package org.allbinary.logic.system.hardware.components.linux

from __future__ import annotations

from org.allbinary.logic.system.hardware.components.interfaces.CpuInterface import CpuInterface
from org.allbinary.logic.system.hardware.components.interfaces.HardwareComponentInterface import HardwareComponentInterface


class Cpu(CpuInterface, HardwareComponentInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.CPUFILE: str = "/proc/cpuinfo"
        self.cpuHashMap: dict = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 0:
            self._constructor0(*args)
    

    def _constructor1(self, filePath: str) -> None:
        self._init_fields()
        self.init(filePath)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.init(self.CPUFILE)
    

    # throws Exception
    def init(self, filePath: str) -> None:
        lineNumberReader: LineNumberReader = None
        try:
            self.init(lineNumberReader, filePath)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OS):
                self.logUtil.put(str(StringMaker().append("Cpu Data: ").append(str(self))), self, self.commonStrings.CONSTRUCTOR, e)
            raise e
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def init(self, lineNumberReader: LineNumberReader, filePath: str) -> None:
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        try:
            fileReader: FileReader = FileReader(filePath)
            lineNumberReader = LineNumberReader(fileReader)
            self.cpuHashMap = StdUtil.getInstance().createHashMap()
            if lineNumberReader is None:
                fileVector: BasicArrayList = SubDirectory.getInstance().search(filePath, AbFile.createAbFile(FilePathData.getInstance().PATH_START))
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OS):
                    self.logUtil.putF(str(StringMaker().append("Cpu File BasicArrayList Size: ").appendint(fileVector.size())), self, self.commonStrings.CONSTRUCTOR)
                if not fileVector.isEmpty():
                    file: AbFile = fileVector.get(0)
                    lineNumberReader = LineNumberReader(FileReader(file.getPath()))
            if lineNumberReader is not None:
                nextLine: str = lineNumberReader.readLine()
                while lineNumberReader is not None and nextLine is not None:
                    index: int = nextLine.find(':')
                    if index >= 0:
                        key: str = nextLine[0:index]
                        valueIndex: int = index + 1
                        value: str = nextLine[valueIndex:len(nextLine)]
                        if key.find(str(CpuInfo.PROCESSOR)) >= 0:
                            self.cpuHashMap.put(CpuInfo.PROCESSOR, value)
                        if key.find(str(CpuInfo.VENDORID)) >= 0:
                            self.cpuHashMap.put(CpuInfo.VENDORID, value)
                        if key.find(str(CpuInfo.CPUFAMILY)) >= 0:
                            self.cpuHashMap.put(CpuInfo.CPUFAMILY, value)
                        if key.find(str(CpuInfo.MODEL)) >= 0:
                            self.cpuHashMap.put(CpuInfo.MODEL, value)
                        if key.find(str(CpuInfo.MODELNAME)) >= 0:
                            self.cpuHashMap.put(CpuInfo.MODELNAME, value)
                        if key.find(str(CpuInfo.STEPPING)) >= 0:
                            self.cpuHashMap.put(CpuInfo.STEPPING, value)
                        if key.find(str(CpuInfo.CPUMHZ)) >= 0:
                            self.cpuHashMap.put(CpuInfo.CPUMHZ, value)
                        if key.find(str(CpuInfo.CACHESIZE)) >= 0:
                            self.cpuHashMap.put(CpuInfo.CACHESIZE, value)
                    nextLine = lineNumberReader.readLine()
        finally:
            if lineNumberReader is not None:
                lineNumberReader.close()
    

    def getProcessor(self) -> str:
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        return self.cpuHashMap.get(CpuInfo.PROCESSOR)
    

    def getVendorId(self) -> str:
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        return self.cpuHashMap.get(CpuInfo.VENDORID)
    

    def getCpuFamily(self) -> str:
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        return self.cpuHashMap.get(CpuInfo.CPUFAMILY)
    

    def getModel(self) -> str:
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        return self.cpuHashMap.get(CpuInfo.MODEL)
    

    def getModelName(self) -> str:
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        return self.cpuHashMap.get(CpuInfo.MODELNAME)
    

    def getStepping(self) -> str:
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        return self.cpuHashMap.get(CpuInfo.STEPPING)
    

    def getCpuSpeed(self) -> str:
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        return self.cpuHashMap.get(CpuInfo.CPUMHZ)
    

    def getCacheSize(self) -> str:
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        return self.cpuHashMap.get(CpuInfo.CACHESIZE)
    

    def compareTo(self, cpuInterface: CpuInterface) -> bool:
        return True
    

    # Java overloaded method: Python keeps the last definition
    def compareTo(self, componentInterface: HardwareComponentInterface) -> bool:
        return True
    

    def toString(self) -> str:
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        from org.allbinary.logic.system.hardware.components.linux.CpuInfo import CpuInfo
        commonLabels: CommonLabels = CommonLabels.getInstance()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        stringMaker: StringMaker = StringMaker()
        stringMaker.append(str(CpuInfo.PROCESSOR)).append(commonLabels.COLON_SEP).append(self.getProcessor())
        stringMaker.append(commonSeps.NEW_LINE)
        stringMaker.append(str(CpuInfo.VENDORID)).append(commonLabels.COLON_SEP).append(self.getVendorId())
        stringMaker.append(commonSeps.NEW_LINE)
        stringMaker.append(str(CpuInfo.CPUFAMILY)).append(commonLabels.COLON_SEP).append(self.getCpuFamily())
        stringMaker.append(commonSeps.NEW_LINE)
        stringMaker.append(str(CpuInfo.MODEL)).append(commonLabels.COLON_SEP).append(self.getModel())
        stringMaker.append(commonSeps.NEW_LINE)
        stringMaker.append(str(CpuInfo.MODELNAME)).append(commonLabels.COLON_SEP).append(self.getModelName())
        stringMaker.append(commonSeps.NEW_LINE)
        stringMaker.append(str(CpuInfo.STEPPING)).append(commonLabels.COLON_SEP).append(self.getStepping())
        stringMaker.append(commonSeps.NEW_LINE)
        stringMaker.append(str(CpuInfo.CPUMHZ)).append(commonLabels.COLON_SEP).append(self.getCpuSpeed())
        stringMaker.append(commonSeps.NEW_LINE)
        stringMaker.append(str(CpuInfo.CACHESIZE)).append(commonLabels.COLON_SEP).append(self.getCacheSize())
        return str(stringMaker)

    def __str__(self) -> str:
        return self.toString()
# from java.io.FileReader import FileReader
# from java.io.LineNumberReader import LineNumberReader
# from java.util.HashMap import HashMap
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.FilePathData import FilePathData
from org.allbinary.logic.io.file.directory.SubDirectory import SubDirectory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList


