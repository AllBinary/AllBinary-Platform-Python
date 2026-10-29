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



class PCComponentFactory:
    instance: PCComponentFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.componentFactory: ComponentFactory = ComponentFactory.getInstance()
    

    @staticmethod
    def getInstance() -> PCComponentFactory:
        return PCComponentFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, component: str, componentData: str) -> HardwareComponentInterface:
        try:
            if component is not None:
                if ((component > str(self.componentFactory.ETHERNET)) - (component < str(self.componentFactory.ETHERNET))) == 0:
                    return Ethernet(componentData)
                elif ((component > str(self.componentFactory.BRIDGE)) - (component < str(self.componentFactory.BRIDGE))) == 0:
                    return Bridge(componentData)
                elif ((component > str(self.componentFactory.IDE)) - (component < str(self.componentFactory.IDE))) == 0:
                    return HardDriveController(componentData)
                elif ((component > str(self.componentFactory.MULTIMEDIA)) - (component < str(self.componentFactory.MULTIMEDIA))) == 0:
                    return Media(componentData)
                elif ((component > str(self.componentFactory.SCSI)) - (component < str(self.componentFactory.SCSI))) == 0:
                    return HardDriveController(componentData)
                elif ((component > str(self.componentFactory.USB)) - (component < str(self.componentFactory.USB))) == 0:
                    return Usb(componentData)
                elif ((component > str(self.componentFactory.VGA)) - (component < str(self.componentFactory.VGA))) == 0:
                    return Video(componentData)
                elif ((component > str(self.componentFactory.PCI)) - (component < str(self.componentFactory.PCI))) == 0:
                    return PCI(componentData)
            return Unknown(componentData)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().FACTORYERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return Unknown(commonStrings.EXCEPTION)
    

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
        elif ((component > str(self.componentFactory.PCI)) - (component < str(self.componentFactory.PCI))) == 0:
            return str(self.componentFactory.PCI)
        return str(self.componentFactory.UNKNOWN)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.logic.system.hardware.components.ComponentFactory import ComponentFactory
from org.allbinary.logic.system.hardware.components.interfaces.HardwareComponentInterface import HardwareComponentInterface
from org.allbinary.logic.system.hardware.components.linux.Bridge import Bridge
from org.allbinary.logic.system.hardware.components.linux.Ethernet import Ethernet
from org.allbinary.logic.system.hardware.components.linux.HardDriveController import HardDriveController
from org.allbinary.logic.system.hardware.components.linux.Media import Media
from org.allbinary.logic.system.hardware.components.linux.PCI import PCI
from org.allbinary.logic.system.hardware.components.linux.Unknown import Unknown
from org.allbinary.logic.system.hardware.components.linux.Usb import Usb
from org.allbinary.logic.system.hardware.components.linux.Video import Video
from org.allbinary.string.CommonStrings import CommonStrings


PCComponentFactory.instance = PCComponentFactory()

