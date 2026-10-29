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
# package org.allbinary.logic.communication.log

from __future__ import annotations



#NoPlatform
class PreLogUtil:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def put(specialMessage: str, anyType: object, functionName: str) -> None:
        PreLogUtil.putOE(specialMessage, anyType, functionName, NullUtil.getInstance().NULL_OBJECT)
    

    @staticmethod
    def putOE(specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        raise RuntimeError()
    

    @staticmethod
    def putSE(specialMessage: str, className: str, functionName: str, exception: object) -> None:
        raise RuntimeError()
from org.allbinary.logic.NullUtil import NullUtil


