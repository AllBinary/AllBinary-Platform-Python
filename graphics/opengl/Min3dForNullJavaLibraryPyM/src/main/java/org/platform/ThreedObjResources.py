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
# package org.platform

from __future__ import annotations



class ThreedObjResources:
    instance: ThreedObjResources = None

    def _init_fields(self) -> None:
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ThreedObjResources:
        return ThreedObjResources.instance
    

    def get(self, resourceName: str) -> str:
        resourceName2: str = self.hashtable.get(resourceName)
        if resourceName2 is not None:
            return resourceName2
        return resourceName
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable


ThreedObjResources.instance = ThreedObjResources()

