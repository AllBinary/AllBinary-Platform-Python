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


class UnitGameResources(BasicGameResources):
    ICON: str = "_icon"
    BUILD: str = "_build"
    DESTROY: str = "_destroy"
    ICON_BUILD: str = None

    def _init_fields(self) -> None:
        self.NAME: str = StringUtil.getInstance().EMPTY_STRING
        self.RESOURCE_ICON_ANIMATION: str = StringUtil.getInstance().EMPTY_STRING
        self.RESOURCE_ICON_BUILD: str = StringUtil.getInstance().EMPTY_STRING
        self.RESOURCE_ICON: str = StringUtil.getInstance().EMPTY_STRING
        self.ICON_SIZE: str = "_64_by_64.png"
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws Exception
    def append(self, ROOT: str, sizeString: str) -> None:
        super().append(ROOT, sizeString)
        string: str = GameGraphicsResourceUtil.getInstance().getName()
        BasicGameResources.stringBuffer.delete(0, BasicGameResources.stringBuffer.length())
        BasicGameResources.stringBuffer.append(ROOT)
        BasicGameResources.stringBuffer.append(UnitGameResources.DESTROY)
        BasicGameResources.stringBuffer.append(string)
        BasicGameResources.stringBuffer.append(sizeString)
        self.RESOURCE_DESTROY = str(BasicGameResources.stringBuffer)
        BasicGameResources.stringBuffer.delete(0, BasicGameResources.stringBuffer.length())
        BasicGameResources.stringBuffer.append(UnitGameResources.ICON)
        BasicGameResources.stringBuffer.append(ROOT)
        self.RESOURCE_ICON_ANIMATION = str(BasicGameResources.stringBuffer)
        BasicGameResources.stringBuffer.delete(0, BasicGameResources.stringBuffer.length())
        BasicGameResources.stringBuffer.append(ROOT)
        BasicGameResources.stringBuffer.append(UnitGameResources.ICON)
        BasicGameResources.stringBuffer.append(string)
        BasicGameResources.stringBuffer.append(self.ICON_SIZE)
        self.RESOURCE_ICON = str(BasicGameResources.stringBuffer)
        BasicGameResources.stringBuffer.delete(0, BasicGameResources.stringBuffer.length())
        BasicGameResources.stringBuffer.append(ROOT)
        BasicGameResources.stringBuffer.append(UnitGameResources.ICON_BUILD)
        BasicGameResources.stringBuffer.append(string)
        BasicGameResources.stringBuffer.append(self.ICON_SIZE)
        self.RESOURCE_ICON_BUILD = str(BasicGameResources.stringBuffer)
    

    # throws Exception
    def getString(self) -> str:
        if AndroidUtil.isAndroid():
            return GameGraphicsResourceUtil.getInstance().getStringForFeature(GraphicsFeatureFactory.getInstance().SPRITE_QUARTER_ROTATION_GRAPHICS)
        else:
            return super().getString()
from org.allbinary.game.layer.resources.GameGraphicsResourceUtil import GameGraphicsResourceUtil
from org.allbinary.AndroidUtil import AndroidUtil
from org.allbinary.game.configuration.feature.GraphicsFeatureFactory import GraphicsFeatureFactory
from org.allbinary.logic.string.StringUtil import StringUtil


UnitGameResources.ICON_BUILD = "_icon" + str(UnitGameResources.BUILD)

