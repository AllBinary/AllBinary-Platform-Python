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
# package org.allbinary.logic.control.validate

from __future__ import annotations



# Java interface
class ValidatorBaseInterface:
    

    def isValid(self) -> bool:
        raise NotImplementedError()
    

    def validationInfo(self) -> str:
        raise NotImplementedError()
    

    def toHashtable(self) -> ABHashtable[object, object]:
        raise NotImplementedError()
    

    def toList(self) -> BasicArrayList:
        raise NotImplementedError()
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList


