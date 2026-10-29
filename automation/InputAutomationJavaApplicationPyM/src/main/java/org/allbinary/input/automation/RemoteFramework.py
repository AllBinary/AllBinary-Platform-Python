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
# package org.allbinary.input.automation

from __future__ import annotations



# Java interface
class RemoteFramework:
    

    def connect(self, host: str) -> BundleContext:
        raise NotImplementedError()
    

    def disconnect(self, bc: BundleContext) -> None:
        raise NotImplementedError()
    

    def getSystemProperties(self, bc: BundleContext) -> Map:
        raise NotImplementedError()
# from java.util.Map import Map
from org.osgi.framework.BundleContext import BundleContext


