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
# package org.allbinary.data.tables.transform.info

from __future__ import annotations

from org.allbinary.data.tables.BasicDataTableInterface import BasicDataTableInterface


# Java interface
class TransformInfoEntityInterface(BasicDataTableInterface):
    

    # throws Exception
    def get(self, name: str, propertiesHashMap: dict, pageContext: PageContext) -> TransformInfoInterface:
        raise NotImplementedError()
    

    # throws Exception
    def getObjectConfigs(self, storeName: str) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def getNames(self, storeName: str) -> BasicArrayList:
        raise NotImplementedError()
    

    def delete(self, name: str) -> None:
        raise NotImplementedError()
    

    def insert(self, values: BasicArrayList) -> None:
        raise NotImplementedError()
    

    def update(self, updatedValues: dict) -> None:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface


