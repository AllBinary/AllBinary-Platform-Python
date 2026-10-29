# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.logic.system

from __future__ import annotations



class PlatformAssetManager:
    instance: PlatformAssetManager = None
    

    @staticmethod
    def getInstance() -> PlatformAssetManager:
        return PlatformAssetManager.instance
    

    # throws Exception
    def getResourceAsStream(self, resource: str) -> InputStream:
        resourceUtil: ResourceUtil = ResourceUtil.getInstance()
        inputStream: InputStream = resourceUtil.getResourceAsStream(resource)
        return inputStream
# from java.io.InputStream import InputStream
from org.allbinary.data.resource.ResourceUtil import ResourceUtil


PlatformAssetManager.instance = PlatformAssetManager()

