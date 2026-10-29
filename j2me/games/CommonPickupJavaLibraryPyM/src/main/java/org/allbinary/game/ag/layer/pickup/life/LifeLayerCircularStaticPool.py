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
# package org.allbinary.game.ag.layer.pickup.life

from __future__ import annotations

from org.allbinary.layer.AllBinaryLayerCircularPool import AllBinaryLayerCircularPool


class LifeLayerCircularStaticPool(AllBinaryLayerCircularPool):
    

    def __init__(self, allbinaryLayerFactoryInterface: AllBinaryLayerFactoryInterface, total: int) -> None:
        super().__init__()
        super().initAllBinaryLayerCircularPool(allbinaryLayerFactoryInterface, total)
    

    # throws Exception
    def visit(self, sourceLayerInterface: AllBinaryLayer) -> None:
        lifeLayer: LifeLayer = self.getNextInstance()
        lifeInterfaceCompositeInterface: LifeInterfaceCompositeInterface = sourceLayerInterface
        lifeInterface: Life = lifeInterfaceCompositeInterface.getLifeInterface()
        lifeLayer.visit(lifeInterface)
from org.allbinary.game.ag.life.Life import Life
from org.allbinary.game.ag.life.LifeInterfaceCompositeInterface import LifeInterfaceCompositeInterface
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerFactoryInterface import AllBinaryLayerFactoryInterface


