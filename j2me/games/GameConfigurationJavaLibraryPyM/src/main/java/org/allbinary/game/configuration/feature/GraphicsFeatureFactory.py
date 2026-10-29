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
# package org.allbinary.game.configuration.feature

from __future__ import annotations



class GraphicsFeatureFactory:
    instance: GraphicsFeatureFactory = None

    def _init_fields(self) -> None:
        self.NONE: GraphicsFeature = GraphicsFeature(StringUtil.getInstance().NULL_STRING)
        self.TRANSPARENT_IMAGE_CREATION: GraphicsFeature = GraphicsFeature("Transparent Image Creation")
        self.IMAGE_GRAPHICS: GraphicsFeature = GraphicsFeature("Image Graphics")
        self.IMAGE_ROTATION_ON_THE_FLY: GraphicsFeature = GraphicsFeature("Image Rotated On The Fly")
        self.IMAGE_TO_ARRAY_GRAPHICS: GraphicsFeature = GraphicsFeature("Image To Array Graphics")
        self.SPRITE_QUARTER_ROTATION_GRAPHICS: GraphicsFeature = GraphicsFeature("Sprite Quarter Rotation Graphics")
        self.SPRITE_FULL_GRAPHICS: GraphicsFeature = GraphicsFeature("Sprite Full Rotation Graphics")
        self.VECTOR_GRAPHICS: GraphicsFeature = GraphicsFeature("BasicArrayList Graphics")
        self.VECTOR_TO_IMAGE_GRAPHICS: GraphicsFeature = GraphicsFeature("BasicArrayList To Image Graphics")
    

    @staticmethod
    def getInstance() -> GraphicsFeatureFactory:
        return GraphicsFeatureFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.game.configuration.feature.GraphicsFeature import GraphicsFeature


GraphicsFeatureFactory.instance = GraphicsFeatureFactory()

