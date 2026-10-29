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

from org.allbinary.game.combat.destroy.DestroyableBaseBehavior import DestroyableBaseBehavior


class DestroyableSimpleBehavior(DestroyableBaseBehavior):

    def _init_fields(self) -> None:
        self.ownerLayer: CollidableCompositeLayer = None
        self.destroyed: bool = False
    

    def __init__(self, ownerLayer: CollidableCompositeLayer) -> None:
        super().__init__()
        self._init_fields()
        self.ownerLayer = ownerLayer
    

    def isDestroyed(self) -> bool:
        return self.destroyed
    

    def setDestroyed(self, destroyed: bool) -> None:
        from org.allbinary.game.combat.destroy.DestroyedLayerProcessor import DestroyedLayerProcessor
        self.destroyed = destroyed
        if self.isDestroyed():
            DestroyedLayerProcessor.getInstance().add(self.ownerLayer)
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer


