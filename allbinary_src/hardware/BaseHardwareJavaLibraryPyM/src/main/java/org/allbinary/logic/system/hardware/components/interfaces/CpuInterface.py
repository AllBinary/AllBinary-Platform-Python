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
# package org.allbinary.logic.system.hardware.components.interfaces

from __future__ import annotations



# Java interface
class CpuInterface:
    

    def getProcessor(self) -> str:
        raise NotImplementedError()
    

    def getVendorId(self) -> str:
        raise NotImplementedError()
    

    def getCpuFamily(self) -> str:
        raise NotImplementedError()
    

    def getModel(self) -> str:
        raise NotImplementedError()
    

    def getModelName(self) -> str:
        raise NotImplementedError()
    

    def getStepping(self) -> str:
        raise NotImplementedError()
    

    def getCpuSpeed(self) -> str:
        raise NotImplementedError()
    

    def getCacheSize(self) -> str:
        raise NotImplementedError()
    

    def compareTo(self, cpuInterface: CpuInterface) -> bool:
        raise NotImplementedError()


