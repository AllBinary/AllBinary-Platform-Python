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
# package org.allbinary.logic.system.hardware.linux

from __future__ import annotations

from org.allbinary.logic.system.hardware.HardwareInterface import HardwareInterface


class LinuxHardware(HardwareInterface):
    PCIFILE: str = "/proc/pci"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.componentInterfaceVector: BasicArrayList = None
        self.videoInterfaceVector: BasicArrayList = None
        self.hardDriveControllerInterfaceVector: BasicArrayList = None
        self.cpuInterfaceVector: BasicArrayList = None
        self.usbInterfaceVector: BasicArrayList = None
        self.ethernetInterfaceVector: BasicArrayList = None
        self.multimediaInterfaceVector: BasicArrayList = None
        self.fireWireInterfaceVector: BasicArrayList = None
        self.bridgeInterfaceVector: BasicArrayList = None
        self.hardDriveInterfaceVector: BasicArrayList = None
        self.macInterfaceVector: BasicArrayList = None
        self.monitorInterfaceVector: BasicArrayList = None
        self.NAME: str = "Linux Hardware Profile"
        self.MINHARDWARE: int = 5

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 0:
            self._constructor0(*args)
    

    def _constructor1(self, path: str) -> None:
        self._init_fields()
        self.init(path)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.init(LinuxHardware.PCIFILE)
        if self.componentInterfaceVector.size() < self.MINHARDWARE:
            raise Exception("Not Enough Data For A Valid License On Linux")
        cpu: Cpu = Cpu()
        if cpu is not None:
            self.cpuInterfaceVector.add(cpu)
            self.componentInterfaceVector.add(cpu)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OS):
            self.logUtil.putF("Hardware Data: " + str(self), self, self.commonStrings.CONSTRUCTOR)
    

    # throws Exception
    def init(self, filePath: str) -> None:
        lineNumberReader: LineNumberReader = None
        try:
            self.init(lineNumberReader, filePath)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OS):
                self.logUtil.put("Hardware Data: " + str(self), self, self.commonStrings.CONSTRUCTOR, e)
            raise e
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def init(self, lineNumberReader: LineNumberReader, filePath: str) -> None:
        from org.allbinary.logic.system.hardware.linux.PCComponentFactory import PCComponentFactory
        from org.allbinary.logic.system.hardware.linux.PCComponentFactory import PCComponentFactory
        try:
            self.componentInterfaceVector = BasicArrayListD()
            self.videoInterfaceVector = BasicArrayListD()
            self.hardDriveControllerInterfaceVector = BasicArrayListD()
            self.cpuInterfaceVector = BasicArrayListD()
            self.usbInterfaceVector = BasicArrayListD()
            self.ethernetInterfaceVector = BasicArrayListD()
            self.multimediaInterfaceVector = BasicArrayListD()
            self.fireWireInterfaceVector = BasicArrayListD()
            self.bridgeInterfaceVector = BasicArrayListD()
            self.hardDriveInterfaceVector = BasicArrayListD()
            self.macInterfaceVector = BasicArrayListD()
            self.monitorInterfaceVector = BasicArrayListD()
            pciFile: FileReader = FileReader(filePath)
            lineNumberReader = LineNumberReader(pciFile)
            if lineNumberReader is None:
                fileVector: BasicArrayList = SubDirectory.getInstance().search(filePath, AbFile.createAbFile(FilePathData.getInstance().PATH_START))
                if not fileVector.isEmpty():
                    file: AbFile = fileVector.get(0)
                    lineNumberReader = LineNumberReader(FileReader(file.getPath()))
                if lineNumberReader is None:
                    raise Exception("No Linux File Data")
            if lineNumberReader is not None:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OS):
                    self.logUtil.putF("PCI File Found", self, self.commonStrings.CONSTRUCTOR)
                nextLine: str = lineNumberReader.readLine()
                while lineNumberReader is not None and nextLine is not None:
                    if self.isNextHardware(nextLine):
                        break
                    nextLine = lineNumberReader.readLine()
                while self.isNextHardware(nextLine):
                    componentData: StringMaker = StringMaker()
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OS):
                        self.logUtil.putF("Found Hardware Device: " + str(self.componentInterfaceVector.size()), self, self.commonStrings.CONSTRUCTOR)
                    componentData.append(nextLine)
                    componentData.append(CommonSeps.getInstance().NEW_LINE)
                    nextLine = lineNumberReader.readLine()
                    componentType: str = PCComponentFactory.getInstance().getComponentType(nextLine)
                    while lineNumberReader is not None:
                        componentData.append(nextLine)
                        componentData.append(CommonSeps.getInstance().NEW_LINE)
                        nextLine = lineNumberReader.readLine()
                        if nextLine is None or self.isNextHardware(nextLine):
                            break
                    componentInterface: HardwareComponentInterface = PCComponentFactory.getInstance().getInstance(componentType, str(componentData))
                    if componentInterface is not None:
                        self.componentInterfaceVector.add(componentInterface)
            else:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OS):
                    self.logUtil.putF("Could not load PCI File", self, self.commonStrings.CONSTRUCTOR)
            lineNumberReader.close()
        finally:
            if lineNumberReader is not None:
                lineNumberReader.close()
    

    def getMultimedia(self, index: int) -> MediaInterface:
        return self.multimediaInterfaceVector.get(index)
    

    def getBridge(self, index: int) -> BridgeInterface:
        return self.bridgeInterfaceVector.get(index)
    

    def getCpu(self, index: int) -> CpuInterface:
        return self.cpuInterfaceVector.get(index)
    

    def getEthernet(self, index: int) -> EthernetInterface:
        return self.ethernetInterfaceVector.get(index)
    

    def getFireWire(self, index: int) -> FireWireInterface:
        return self.fireWireInterfaceVector.get(index)
    

    def getHardDriveController(self, index: int) -> HardDriveControllerInterface:
        return self.hardDriveControllerInterfaceVector.get(index)
    

    def getHardDrive(self, index: int) -> HardDriveInterface:
        return self.hardDriveInterfaceVector.get(index)
    

    def getMachineAccessControlAddress(self, index: int) -> MachineAccessControlAddressInterface:
        return self.macInterfaceVector.get(index)
    

    def getMonitor(self, index: int) -> MonitorInterface:
        return self.monitorInterfaceVector.get(index)
    

    def getUsb(self, index: int) -> UsbInterface:
        return self.usbInterfaceVector.get(index)
    

    def getVideo(self, index: int) -> VideoInterface:
        return self.videoInterfaceVector.get(index)
    

    def getComponent(self, index: int) -> HardwareComponentInterface:
        return self.componentInterfaceVector.get(index)
    

    def toString(self) -> str:
        hardwareBuffer: StringMaker = StringMaker()
        size: int = self.componentInterfaceVector.size()
        for index in range(0, size):
            componentInterface: HardwareComponentInterface = self.componentInterfaceVector.get(index)
            hardwareBuffer.append("Component ")
            hardwareBuffer.appendint(index)
            hardwareBuffer.append(": \n")
            hardwareBuffer.append(str(componentInterface))
            hardwareBuffer.append(CommonSeps.getInstance().NEW_LINE)
        return str(hardwareBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def compareTo(self, hardwareInterface: HardwareInterface) -> bool:
        return True
    

    def difference(self, hardwareInterface: HardwareInterface) -> ABHashtable[object, object]:
        return StdUtil.getInstance().NULL_TABLE
    

    def isNextHardware(self, nextLine: str) -> bool:
        if nextLine is not None:
            index: int = nextLine.find("Bus")
            if index >= 0 and index < 4:
                return True
        return False
# from java.io.FileReader import FileReader
# from java.io.LineNumberReader import LineNumberReader
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.FilePathData import FilePathData
from org.allbinary.logic.io.file.directory.SubDirectory import SubDirectory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.hardware.components.interfaces.BridgeInterface import BridgeInterface
from org.allbinary.logic.system.hardware.components.interfaces.CpuInterface import CpuInterface
from org.allbinary.logic.system.hardware.components.interfaces.EthernetInterface import EthernetInterface
from org.allbinary.logic.system.hardware.components.interfaces.FireWireInterface import FireWireInterface
from org.allbinary.logic.system.hardware.components.interfaces.HardDriveControllerInterface import HardDriveControllerInterface
from org.allbinary.logic.system.hardware.components.interfaces.HardDriveInterface import HardDriveInterface
from org.allbinary.logic.system.hardware.components.interfaces.HardwareComponentInterface import HardwareComponentInterface
from org.allbinary.logic.system.hardware.components.interfaces.MachineAccessControlAddressInterface import MachineAccessControlAddressInterface
from org.allbinary.logic.system.hardware.components.interfaces.MediaInterface import MediaInterface
from org.allbinary.logic.system.hardware.components.interfaces.MonitorInterface import MonitorInterface
from org.allbinary.logic.system.hardware.components.interfaces.UsbInterface import UsbInterface
from org.allbinary.logic.system.hardware.components.interfaces.VideoInterface import VideoInterface
from org.allbinary.logic.system.hardware.components.linux.Cpu import Cpu
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList


