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
# package org.allbinary.data.tables.workflow

from __future__ import annotations

from org.allbinary.data.tables.BasicDataTableInterface import BasicDataTableInterface


# Java interface
class WorkFlowEntityInterface(BasicDataTableInterface):
    

    def get(self, storeName: str) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception, LicensingException
    # Java overloaded method: Python keeps the last definition
    def get(self, name: str, storeName: str) -> WorkFlowInterface:
        raise NotImplementedError()
    

    def delete(self, name: str, storeName: str) -> None:
        raise NotImplementedError()
    

    def insert(self, values: BasicArrayList) -> None:
        raise NotImplementedError()
    

    def update(self, updatedValues: dict) -> None:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.control.workflow.WorkFlowInterface import WorkFlowInterface
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


