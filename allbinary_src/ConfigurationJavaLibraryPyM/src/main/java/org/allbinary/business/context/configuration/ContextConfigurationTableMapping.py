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
# package org.allbinary.business.context.configuration

from __future__ import annotations

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface


class ContextConfigurationTableMapping(TableMappingInterface):

    def _init_fields(self) -> None:
        if "contextConfigurationInterface" not in vars(self): self.contextConfigurationInterface: ContextConfigurationInterface = None
    

    def __init__(self, contextConfigurationInterface: ContextConfigurationInterface) -> None:
        __class__._init_fields(self)
        self.contextConfigurationInterface = contextConfigurationInterface
    

    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        return hashMap
    

    # throws Exception
    def getKey(self) -> object:
        from org.allbinary.business.context.configuration.ContextConfigurationData import ContextConfigurationData
        return ContextConfigurationData.getInstance().NAME
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        vector: BasicArrayList = BasicArrayListD()
        return vector
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.StdUtil import StdUtil


