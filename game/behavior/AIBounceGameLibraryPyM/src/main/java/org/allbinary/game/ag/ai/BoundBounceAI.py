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
# package org.allbinary.game.ag.ai

from __future__ import annotations

from org.allbinary.game.ai.BasicAI import BasicAI


class BoundBounceAI(BasicAI):

    def _init_fields(self) -> None:
        from org.allbinary.bounds.BoundsVisitorInterface import BoundsVisitorInterface
        from org.allbinary.bounds.LayerBounds import LayerBounds
        self.currentRelativeAngle: int = 0
        self.layerBounds: LayerBounds = None
        self.boundsVisitorInterface: BoundsVisitorInterface = None
    

    def __init__(self, ownerLayerInterface: AllBinaryLayer, gameInput: GameInput, layerBounds: LayerBounds, boundsVisitorInterface: BoundsVisitorInterface) -> None:
        from org.allbinary.bounds.BoundsVisitorInterface import BoundsVisitorInterface
        from org.allbinary.bounds.LayerBounds import LayerBounds
        from org.allbinary.game.input.GameInput import GameInput
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        self.layerBounds = layerBounds
        self.boundsVisitorInterface = boundsVisitorInterface
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.Rectangle import Rectangle
        rectange: Rectangle = self.layerBounds.getRectangleP()
        graphics.drawRect(rectange.getPoint().getX(), rectange.getPoint().getY(), rectange.getWidth(), rectange.getHeight())
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        self.layerBounds.visit(self.boundsVisitorInterface)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.bounds.BoundsVisitorInterface import BoundsVisitorInterface
# from org.allbinary.bounds.LayerBounds import LayerBounds
# from org.allbinary.game.input.GameInput import GameInput
# from org.allbinary.graphics.Rectangle import Rectangle
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


