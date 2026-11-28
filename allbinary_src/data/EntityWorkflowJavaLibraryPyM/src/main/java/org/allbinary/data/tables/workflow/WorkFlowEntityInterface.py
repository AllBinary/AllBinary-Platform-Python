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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.data.tables.BasicDataTableInterface import BasicDataTableInterface


# Java interface
@java_inherited_overloads
class WorkFlowEntityInterface(BasicDataTableInterface):
    

    def get_j1(self, storeName: str) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise NotImplementedError()
    

    # throws Exception, LicensingException
    def get_j2(self, name: str, storeName: str) -> WorkFlowInterface:
        from org.allbinary.logic.control.workflow.WorkFlowInterface import WorkFlowInterface
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        raise NotImplementedError()

    def get(self, *args):
        implementation = __class__.__dict__.get("get_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().get(*args)
    

    def delete(self, name: str, storeName: str) -> None:
        raise NotImplementedError()
    

    def insert(self, values: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise NotImplementedError()
    

    def update(self, updatedValues: HashMap) -> None:
        from java.util.HashMap import HashMap
        raise NotImplementedError()
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.control.workflow.WorkFlowInterface import WorkFlowInterface
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


