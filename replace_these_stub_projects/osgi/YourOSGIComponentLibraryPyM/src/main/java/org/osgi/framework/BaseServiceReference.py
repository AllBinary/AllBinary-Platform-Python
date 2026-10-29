# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.osgi.framework

from __future__ import annotations

from org.osgi.framework.ServiceReference import ServiceReference


class BaseServiceReference(ServiceReference):
    

    def getProperty(self, key: str) -> object:
        raise RuntimeError()
    

    def getPropertyKeys(self) -> list[str]:
        raise RuntimeError()
    

    def compareTo(self, o: object) -> int:
        raise RuntimeError()


