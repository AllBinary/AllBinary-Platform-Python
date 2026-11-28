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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.ai.BasicAI import BasicAI


@java_inherited_overloads
class BoundBounceAI(BasicAI):
    def _java_defaults(self):
        vars(self).setdefault("currentRelativeAngle", 0)
        vars(self).setdefault("layerBounds", None)
        vars(self).setdefault("boundsVisitorInterface", None)

    def _init_fields(self) -> None:
        self.currentRelativeAngle: int = 0
        if "layerBounds" not in vars(self): self.layerBounds: LayerBounds = None
        if "boundsVisitorInterface" not in vars(self): self.boundsVisitorInterface: BoundsVisitorInterface = None
    

    def __init__(self, ownerLayerInterface: AllBinaryLayer, gameInput: GameInput, layerBounds: LayerBounds, boundsVisitorInterface: BoundsVisitorInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.bounds.BoundsVisitorInterface import BoundsVisitorInterface
        from org.allbinary.bounds.LayerBounds import LayerBounds
        from org.allbinary.game.input.GameInput import GameInput
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        super().__init__(ownerLayerInterface, gameInput)
        __class__._init_fields(self)
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


