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
# package org.allbinary.game.combat.destroy

from __future__ import annotations

from org.allbinary.game.combat.destroy.DestroyableInterface import DestroyableInterface


class DestroyableBaseBehavior(DestroyableInterface):
    instance: DestroyableBaseBehavior = None
    

    @staticmethod
    def getInstance() -> DestroyableBaseBehavior:
        return DestroyableBaseBehavior.instance
    

    def getName(self) -> str:
        return type(self).__module__ + "." + type(self).__qualname__
    

    # throws Exception
    def isDestroyed(self) -> bool:
        raise Exception(CommonStrings.getInstance().NOT_IMPLEMENTED)
    

    def setDestroyed(self, destroyed: bool) -> None:
        pass
from org.allbinary.string.CommonStrings import CommonStrings


DestroyableBaseBehavior.instance = DestroyableBaseBehavior()

