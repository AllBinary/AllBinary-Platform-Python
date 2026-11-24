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
# package org.allbinary.logic.system.hardware.windows

from __future__ import annotations

from org.allbinary.logic.system.hardware.HardwareInterface import HardwareInterface


class WindowsHardware(HardwareInterface):

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.system.hardware.components.ComponentFactory import ComponentFactory
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
        self.NAME: str = "Windows Hardware Profile"
        self.MINHARDWARE: int = 0
        self.componentFactory: ComponentFactory = ComponentFactory.getInstance()
    

    def __init__(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self._init_fields()
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
            if self.componentInterfaceVector.size() < self.MINHARDWARE:
                raise Exception("Not Enough Data For A Valid License On Windows")
        except Exception as e:
            raise e
    

    def getComponentType(self, component: str) -> str:
        if component.find(str(self.componentFactory.ETHERNET)) >= 0:
            return str(self.componentFactory.ETHERNET)
        elif component.find(str(self.componentFactory.BRIDGE)) >= 0:
            return str(self.componentFactory.BRIDGE)
        elif component.find(str(self.componentFactory.IDE)) >= 0:
            return str(self.componentFactory.IDE)
        elif component.find(str(self.componentFactory.MULTIMEDIA)) >= 0:
            return str(self.componentFactory.MULTIMEDIA)
        elif component.find(str(self.componentFactory.SCSI)) >= 0:
            return str(self.componentFactory.SCSI)
        elif component.find(str(self.componentFactory.USB)) >= 0:
            return str(self.componentFactory.USB)
        elif component.find(str(self.componentFactory.VGA)) >= 0:
            return str(self.componentFactory.VGA)
        else:
            return None
    

    def getMultimedia(self, index: int) -> MediaInterface:
        from org.allbinary.logic.system.hardware.components.interfaces.MediaInterface import MediaInterface
        return self.multimediaInterfaceVector.get(index)
    

    def getBridge(self, index: int) -> BridgeInterface:
        from org.allbinary.logic.system.hardware.components.interfaces.BridgeInterface import BridgeInterface
        return self.bridgeInterfaceVector.get(index)
    

    def getCpu(self, index: int) -> CpuInterface:
        from org.allbinary.logic.system.hardware.components.interfaces.CpuInterface import CpuInterface
        return self.cpuInterfaceVector.get(index)
    

    def getEthernet(self, index: int) -> EthernetInterface:
        from org.allbinary.logic.system.hardware.components.interfaces.EthernetInterface import EthernetInterface
        return self.ethernetInterfaceVector.get(index)
    

    def getFireWire(self, index: int) -> FireWireInterface:
        from org.allbinary.logic.system.hardware.components.interfaces.FireWireInterface import FireWireInterface
        return self.fireWireInterfaceVector.get(index)
    

    def getHardDriveController(self, index: int) -> HardDriveControllerInterface:
        from org.allbinary.logic.system.hardware.components.interfaces.HardDriveControllerInterface import HardDriveControllerInterface
        return self.hardDriveControllerInterfaceVector.get(index)
    

    def getHardDrive(self, index: int) -> HardDriveInterface:
        from org.allbinary.logic.system.hardware.components.interfaces.HardDriveInterface import HardDriveInterface
        return self.hardDriveInterfaceVector.get(index)
    

    def getMachineAccessControlAddress(self, index: int) -> MachineAccessControlAddressInterface:
        from org.allbinary.logic.system.hardware.components.interfaces.MachineAccessControlAddressInterface import MachineAccessControlAddressInterface
        return self.macInterfaceVector.get(index)
    

    def getMonitor(self, index: int) -> MonitorInterface:
        from org.allbinary.logic.system.hardware.components.interfaces.MonitorInterface import MonitorInterface
        return self.monitorInterfaceVector.get(index)
    

    def getUsb(self, index: int) -> UsbInterface:
        from org.allbinary.logic.system.hardware.components.interfaces.UsbInterface import UsbInterface
        return self.usbInterfaceVector.get(index)
    

    def getVideo(self, index: int) -> VideoInterface:
        from org.allbinary.logic.system.hardware.components.interfaces.VideoInterface import VideoInterface
        return self.videoInterfaceVector.get(index)
    

    def getComponent(self, index: int) -> HardwareComponentInterface:
        from org.allbinary.logic.system.hardware.components.interfaces.HardwareComponentInterface import HardwareComponentInterface
        return self.componentInterfaceVector.get(index)
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.system.hardware.components.interfaces.HardwareComponentInterface import HardwareComponentInterface
        from org.allbinary.string.CommonSeps import CommonSeps
        hardwareBuffer: StringMaker = StringMaker()
        size: int = self.componentInterfaceVector.size()
        for index in range(0, size):
            componentInterface: HardwareComponentInterface = self.componentInterfaceVector.get(index)
            hardwareBuffer.append(str(componentInterface))
            hardwareBuffer.append(CommonSeps.getInstance().NEW_LINE)
        return str(hardwareBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def compareTo(self, hardwareInterface: HardwareInterface) -> bool:
        return True
    

    def difference(self, hardwareInterface: HardwareInterface) -> ABHashtable[object, object]:
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.util.ABHashtable import ABHashtable
        return StdUtil.getInstance().NULL_TABLE
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.system.hardware.components.ComponentFactory import ComponentFactory
# from org.allbinary.logic.system.hardware.components.interfaces.BridgeInterface import BridgeInterface
# from org.allbinary.logic.system.hardware.components.interfaces.CpuInterface import CpuInterface
# from org.allbinary.logic.system.hardware.components.interfaces.EthernetInterface import EthernetInterface
# from org.allbinary.logic.system.hardware.components.interfaces.FireWireInterface import FireWireInterface
# from org.allbinary.logic.system.hardware.components.interfaces.HardDriveControllerInterface import HardDriveControllerInterface
# from org.allbinary.logic.system.hardware.components.interfaces.HardDriveInterface import HardDriveInterface
# from org.allbinary.logic.system.hardware.components.interfaces.HardwareComponentInterface import HardwareComponentInterface
# from org.allbinary.logic.system.hardware.components.interfaces.MachineAccessControlAddressInterface import MachineAccessControlAddressInterface
# from org.allbinary.logic.system.hardware.components.interfaces.MediaInterface import MediaInterface
# from org.allbinary.logic.system.hardware.components.interfaces.MonitorInterface import MonitorInterface
# from org.allbinary.logic.system.hardware.components.interfaces.UsbInterface import UsbInterface
# from org.allbinary.logic.system.hardware.components.interfaces.VideoInterface import VideoInterface
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.util.ABHashtable import ABHashtable


