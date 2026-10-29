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
    

    def __init__(self) -> None:
        pass
    

    def getMultimedia(self, index: int) -> MediaInterface:
        raise RuntimeError()
    

    def getBridge(self, index: int) -> BridgeInterface:
        raise RuntimeError()
    

    def getCpu(self, index: int) -> CpuInterface:
        raise RuntimeError()
    

    def getEthernet(self, index: int) -> EthernetInterface:
        raise RuntimeError()
    

    def getFireWire(self, index: int) -> FireWireInterface:
        raise RuntimeError()
    

    def getHardDriveController(self, index: int) -> HardDriveControllerInterface:
        raise RuntimeError()
    

    def getHardDrive(self, index: int) -> HardDriveInterface:
        raise RuntimeError()
    

    def getMachineAccessControlAddress(self, index: int) -> MachineAccessControlAddressInterface:
        raise RuntimeError()
    

    def getMonitor(self, index: int) -> MonitorInterface:
        raise RuntimeError()
    

    def getUsb(self, index: int) -> UsbInterface:
        raise RuntimeError()
    

    def getVideo(self, index: int) -> VideoInterface:
        raise RuntimeError()
    

    def getComponent(self, index: int) -> HardwareComponentInterface:
        raise RuntimeError()
    

    def toString(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING

    def __str__(self) -> str:
        return self.toString()
    

    def compareTo(self, hardwareInterface: HardwareInterface) -> bool:
        return True
    

    def difference(self, hardwareInterface: HardwareInterface) -> ABHashtable[object, object]:
        return StdUtil.getInstance().NULL_TABLE
    

    def isNextHardware(self, nextLine: str) -> bool:
        return False
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringUtil import StringUtil
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
from org.allbinary.util.ABHashtable import ABHashtable


