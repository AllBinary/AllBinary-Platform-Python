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
# package org.allbinary.logic.system.security.licensing

from __future__ import annotations



class InApplicationPurchaseFactory:
    instance: InApplicationPurchaseFactory = None
    

    @staticmethod
    def getInstance() -> InApplicationPurchaseFactory:
        return InApplicationPurchaseFactory.instance
    

    def __init__(self) -> None:
        pass
    

    def init(self, anyType: object, stateObject: object) -> None:
        pass
    

    def onCreate(self, anyType: object, stateObject: object) -> None:
        pass
    

    def onStart(self) -> None:
        pass
    

    def onResult(self, requestCode: int, resultCode: int, data: object) -> None:
        pass
    

    def onSaveState(self, anyType: object) -> None:
        pass
    

    def onStop(self) -> None:
        pass
    

    def onDestroy(self) -> None:
        pass
    

    def purchase(self, lockableFeature: LockableFeature) -> None:
        pass
    

    def isPurchased(self, lockableFeature: LockableFeature) -> bool:
        return False
    

    def add(self, lockableFeature: LockableFeature) -> None:
        pass
    

    def getUserName(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def isEnabled(self) -> bool:
        return False
from org.allbinary.logic.string.StringUtil import StringUtil


InApplicationPurchaseFactory.instance = InApplicationPurchaseFactory()

