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
# package org.allbinary.data.tables

from __future__ import annotations



# Java interface
class TableMappingInterface:
    

    # throws Exception
    def getKey(self) -> object:
        raise NotImplementedError()
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def toHashMap(self) -> dict:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList


