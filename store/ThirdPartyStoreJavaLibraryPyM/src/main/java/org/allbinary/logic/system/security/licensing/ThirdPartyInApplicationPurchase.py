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

from org.allbinary.logic.system.security.licensing.ThirdPartyInApplicationPurchaseInterface import ThirdPartyInApplicationPurchaseInterface


class ThirdPartyInApplicationPurchase(ThirdPartyInApplicationPurchaseInterface):
    

    def isPurchased(self, lockableFeature: LockableFeature) -> bool:
        return False
    

    def onCreate(self, anyType: object, stateObject: object) -> None:
        pass
    

    def onDestroy(self) -> None:
        pass
    

    def onStart(self) -> None:
        pass
    

    def onActivityResult(self, requestCode: int, resultCode: int, dataObject: object) -> None:
        pass
    

    def onSaveInstanceState(self, anyType: object) -> None:
        pass
    

    def onStop(self) -> None:
        pass
    

    def requestPurchase(self, lockableFeature: LockableFeature) -> None:
        pass
    

    def requestReceipts(self) -> None:
        pass
    

    def add(self, lockableFeature: LockableFeature) -> None:
        pass
    

    def getUserName(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def isEnabled(self) -> bool:
        return False
    

    def requestProducts(self) -> None:
        pass
from org.allbinary.logic.string.StringUtil import StringUtil


