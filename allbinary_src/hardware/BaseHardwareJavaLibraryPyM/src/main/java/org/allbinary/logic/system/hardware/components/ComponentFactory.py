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
# package org.allbinary.logic.system.hardware.components

from __future__ import annotations



class ComponentFactory:
    instance: ComponentFactory = None

    def _init_fields(self) -> None:
        self.VGA: Component = Component("VGA")
        self.IDE: Component = Component("IDE")
        self.SCSI: Component = Component("SCSI")
        self.BRIDGE: Component = Component("bridge")
        self.ETHERNET: Component = Component("Ethernet")
        self.USB: Component = Component("USB")
        self.MULTIMEDIA: Component = Component("Multimedia")
        self.PCI: Component = Component("PCI")
        self.RAID: Component = Component("RAID")
        self.SMBUS: Component = Component("SMBus")
        self.PIC: Component = Component("PIC")
        self.Class: Component = Component("Class")
        self.UNKNOWN: Component = Component(CommonStrings.getInstance().UNKNOWN)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ComponentFactory:
        return ComponentFactory.instance
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.system.hardware.components.Component import Component


ComponentFactory.instance = ComponentFactory()

