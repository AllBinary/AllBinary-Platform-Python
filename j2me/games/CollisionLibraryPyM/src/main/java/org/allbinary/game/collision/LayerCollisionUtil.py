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
# package org.allbinary.game.collision

from __future__ import annotations



class LayerCollisionUtil:
    instance: LayerCollisionUtil = None

    def _init_fields(self) -> None:
        self.collisionProcessor: CollisionProcessor = None
    

    @staticmethod
    def getInstance() -> LayerCollisionUtil:
        return LayerCollisionUtil.instance
    

    def __init__(self) -> None:
        from org.allbinary.game.collision.Collision2DProcessor import Collision2DProcessor
        from org.allbinary.game.collision.CollisionThreedProcessor import CollisionThreedProcessor
        self._init_fields()
        features: Features = Features.getInstance()
        gameFeatureFactory: GameFeatureFactory = GameFeatureFactory.getInstance()
        if OpenGLFeatureUtil.getInstance().isAnyThreed() and not features.isFeature(gameFeatureFactory.COLLISIONS_FORCED_TWO_DIMENSIONAL):
            self.collisionProcessor = CollisionThreedProcessor()
        else:
            self.collisionProcessor = Collision2DProcessor()
    

    def isCollision(self, myLayer: AllBinaryLayer, myLayer2: AllBinaryLayer) -> bool:
        return self.collisionProcessor.isCollision(myLayer, myLayer2)
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


LayerCollisionUtil.instance = LayerCollisionUtil()

