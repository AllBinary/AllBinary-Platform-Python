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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.layer.resources.BasicGameResources import BasicGameResources


class Unit2DecalGameResources(BasicGameResources):
    instance: object = None
    

    @staticmethod
    def getInstance() -> BasicGameResources:
        from org.allbinary.logic.NullUtil import NullUtil
        if Unit2DecalGameResources.instance == NullUtil.getInstance().NULL_OBJECT:
            Unit2DecalGameResources.instance = Unit2DecalGameResources()
        return Unit2DecalGameResources.instance
    

    def __init__(self) -> None:
        super().__init__()
        ROOT: str = "/unit_decal"
        SMALL: str = "_30_by_30.png"
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
        from org.allbinary.game.layer.resources.GameGraphicsResourceUtil import GameGraphicsResourceUtil
        from org.allbinary.AndroidUtil import AndroidUtil
        from org.allbinary.game.configuration.feature.GraphicsFeatureFactory import GraphicsFeatureFactory
        if AndroidUtil.isAndroid():
            return GameGraphicsResourceUtil.getInstance().getStringForFeature(GraphicsFeatureFactory.getInstance().SPRITE_QUARTER_ROTATION_GRAPHICS)
        else:
            return super().getString()
# from org.allbinary.game.layer.resources.GameGraphicsResourceUtil import GameGraphicsResourceUtil
# from org.allbinary.AndroidUtil import AndroidUtil
# from org.allbinary.game.configuration.feature.GraphicsFeatureFactory import GraphicsFeatureFactory
# from org.allbinary.logic.NullUtil import NullUtil


def _Unit2DecalGameResources_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(Unit2DecalGameResources, "instance", _Unit2DecalGameResources_instance)

