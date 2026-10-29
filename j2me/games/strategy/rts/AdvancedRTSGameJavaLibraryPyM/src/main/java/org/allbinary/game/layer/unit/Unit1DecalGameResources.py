# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.layer.unit

from __future__ import annotations

from org.allbinary.game.layer.resources.BasicGameResources import BasicGameResources


class Unit1DecalGameResources(BasicGameResources):
    instance: Unit1DecalGameResources = None
    

    def __init__(self) -> None:
        super().__init__()
        ROOT: str = "/unit_decal"
        SMALL: str = "_20_by_20.png"
        MEDIUM: str = SMALL
        SIZE_FOUR: str = SMALL
        SIZE_FIVE: str = SMALL
        SIZE_SIX: str = SMALL
        SIZE: list[str] = [SMALL, MEDIUM, SIZE_FOUR, SIZE_FIVE, SIZE_SIX]
        super().init(ROOT, SIZE)
    

    # throws Exception
    def append(self, ROOT: str, sizeString: str) -> None:
        super().append(ROOT, sizeString)
    

    # throws Exception
    def getString(self) -> str:
        if AndroidUtil.isAndroid():
            return GameGraphicsResourceUtil.getInstance().getStringForFeature(GraphicsFeatureFactory.getInstance().SPRITE_QUARTER_ROTATION_GRAPHICS)
        else:
            return super().getString()
    

    @staticmethod
    def getInstance() -> BasicGameResources:
        return Unit1DecalGameResources.instance
from org.allbinary.game.layer.resources.GameGraphicsResourceUtil import GameGraphicsResourceUtil
from org.allbinary.AndroidUtil import AndroidUtil
from org.allbinary.game.configuration.feature.GraphicsFeatureFactory import GraphicsFeatureFactory


Unit1DecalGameResources.instance = Unit1DecalGameResources()

