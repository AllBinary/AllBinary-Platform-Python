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



# Java interface
class ThirdPartyInApplicationPurchaseInterface:
    

    def isPurchased(self, lockableFeature: LockableFeature) -> bool:
        raise NotImplementedError()
    

    def onCreate(self, anyType: object, stateObject: object) -> None:
        raise NotImplementedError()
    

    def onDestroy(self) -> None:
        raise NotImplementedError()
    

    def onStart(self) -> None:
        raise NotImplementedError()
    

    def onActivityResult(self, requestCode: int, resultCode: int, dataObject: object) -> None:
        raise NotImplementedError()
    

    def onSaveInstanceState(self, anyType: object) -> None:
        raise NotImplementedError()
    

    def onStop(self) -> None:
        raise NotImplementedError()
    

    def requestPurchase(self, lockableFeature: LockableFeature) -> None:
        raise NotImplementedError()
    

    def requestReceipts(self) -> None:
        raise NotImplementedError()
    

    def add(self, lockableFeature: LockableFeature) -> None:
        raise NotImplementedError()
    

    def getUserName(self) -> str:
        raise NotImplementedError()
    

    def isEnabled(self) -> bool:
        raise NotImplementedError()


