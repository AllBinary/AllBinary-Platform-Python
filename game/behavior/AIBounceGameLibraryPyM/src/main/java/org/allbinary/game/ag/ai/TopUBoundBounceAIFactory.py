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

from org.allbinary.game.ai.ArtificialIntelligenceInterfaceFactoryInterface import ArtificialIntelligenceInterfaceFactoryInterface


class TopUBoundBounceAIFactory(ArtificialIntelligenceInterfaceFactoryInterface):
    

    # throws Exception
    def getInstance(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> ArtificialIntelligenceInterface:
        from org.allbinary.game.ag.ai.BoundBounceAI import BoundBounceAI
        from org.allbinary.game.ag.ai.ReverseVelocityBoundsVisitor import ReverseVelocityBoundsVisitor
        velocityInterfaceCompositeInterface: VelocityInterfaceCompositeInterface = ownerLayerInterface
        velocityInterface: VelocityInterface = velocityInterfaceCompositeInterface.getVelocityProperties()
        maxDistancePerTick: int = (velocityInterface.getMaxForwardVelocity() >> velocityInterface.getVelocityXBasicDecimalP().getScaledFactor())
        halfWidth: int = ownerLayerInterface.getWidth() * 2 + maxDistancePerTick + 1
        halfHeight: int = ownerLayerInterface.getHeight() * 2 + maxDistancePerTick + 1
        point: GPoint = PointFactory.getInstance().createXY(halfWidth, halfHeight + 60)
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        rectangle: Rectangle = Rectangle(point, (displayInfo.getLastWidth() - halfWidth - point.getX()), (displayInfo.getLastHeight() - halfHeight - point.getY()))
        return BoundBounceAI(ownerLayerInterface, gameInput, TopULayerBounds(rectangle), ReverseVelocityBoundsVisitor(ownerLayerInterface))
from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
from org.allbinary.bounds.TopULayerBounds import TopULayerBounds
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.physics.velocity.VelocityInterface import VelocityInterface
from org.allbinary.game.physics.velocity.VelocityInterfaceCompositeInterface import VelocityInterfaceCompositeInterface
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.util.ABHashtable import ABHashtable


