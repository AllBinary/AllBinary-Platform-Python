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



class CollidableHelperFactory:
    

    @staticmethod
    def getInstance() -> CollisionHelper:
        from org.allbinary.game.collision.SourceCollisionHelper import SourceCollisionHelper
        from org.allbinary.game.collision.CollisionHelper import CollisionHelper
        if Features.getInstance().isFeature(GameFeatureFactory.getInstance().COLLISIONS_WITH_SOURCE):
            return CollisionHelper(AllBinaryLayer.NULL_ALLBINARY_LAYER)
        else:
            return SourceCollisionHelper(AllBinaryLayer.NULL_ALLBINARY_LAYER)
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


