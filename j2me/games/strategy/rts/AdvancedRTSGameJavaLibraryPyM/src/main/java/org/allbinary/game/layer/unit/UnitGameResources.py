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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.layer.resources.BasicGameResources import BasicGameResources


@java_inherited_overloads
class UnitGameResources(BasicGameResources):
    ICON: str = "_icon"
    BUILD: str = "_build"
    DESTROY: str = "_destroy"
    ICON_BUILD: str = None
    def _java_defaults(self):
        vars(self).setdefault("NAME", None)
        vars(self).setdefault("RESOURCE_ICON_ANIMATION", None)
        vars(self).setdefault("RESOURCE_ICON_BUILD", None)
        vars(self).setdefault("RESOURCE_ICON", None)
        vars(self).setdefault("ICON_SIZE", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.NAME: str = StringUtil.getInstance().EMPTY_STRING
        self.RESOURCE_ICON_ANIMATION: str = StringUtil.getInstance().EMPTY_STRING
        self.RESOURCE_ICON_BUILD: str = StringUtil.getInstance().EMPTY_STRING
        self.RESOURCE_ICON: str = StringUtil.getInstance().EMPTY_STRING
        self.ICON_SIZE: str = "_64_by_64.png"
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    # throws Exception
    def append(self, ROOT: str, sizeString: str) -> None:
        from org.allbinary.game.layer.resources.GameGraphicsResourceUtil import GameGraphicsResourceUtil
        java_super_call(super(), "append", ROOT, sizeString)
        string: str = GameGraphicsResourceUtil.getInstance().getName()
        BasicGameResources.stringBuffer.delete(0, __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(BasicGameResources.stringBuffer))
        BasicGameResources.stringBuffer.append(ROOT)
        BasicGameResources.stringBuffer.append(UnitGameResources.DESTROY)
        BasicGameResources.stringBuffer.append(string)
        BasicGameResources.stringBuffer.append(sizeString)
        self.RESOURCE_DESTROY = str(BasicGameResources.stringBuffer)
        BasicGameResources.stringBuffer.delete(0, __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(BasicGameResources.stringBuffer))
        BasicGameResources.stringBuffer.append(UnitGameResources.ICON)
        BasicGameResources.stringBuffer.append(ROOT)
        self.RESOURCE_ICON_ANIMATION = str(BasicGameResources.stringBuffer)
        BasicGameResources.stringBuffer.delete(0, __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(BasicGameResources.stringBuffer))
        BasicGameResources.stringBuffer.append(ROOT)
        BasicGameResources.stringBuffer.append(UnitGameResources.ICON)
        BasicGameResources.stringBuffer.append(string)
        BasicGameResources.stringBuffer.append(self.ICON_SIZE)
        self.RESOURCE_ICON = str(BasicGameResources.stringBuffer)
        BasicGameResources.stringBuffer.delete(0, __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(BasicGameResources.stringBuffer))
        BasicGameResources.stringBuffer.append(ROOT)
        BasicGameResources.stringBuffer.append(UnitGameResources.ICON_BUILD)
        BasicGameResources.stringBuffer.append(string)
        BasicGameResources.stringBuffer.append(self.ICON_SIZE)
        self.RESOURCE_ICON_BUILD = str(BasicGameResources.stringBuffer)
    

    # throws Exception
    def getString(self) -> str:
        from org.allbinary.game.layer.resources.GameGraphicsResourceUtil import GameGraphicsResourceUtil
        from org.allbinary.AndroidUtil import AndroidUtil
        from org.allbinary.game.configuration.feature.GraphicsFeatureFactory import GraphicsFeatureFactory
        if java_predicate(AndroidUtil, "isAndroid"):
            return GameGraphicsResourceUtil.getInstance().getStringForFeature(GraphicsFeatureFactory.getInstance().SPRITE_QUARTER_ROTATION_GRAPHICS)
        else:
            return java_super_call(super(), "getString")
# from org.allbinary.game.layer.resources.GameGraphicsResourceUtil import GameGraphicsResourceUtil
# from org.allbinary.AndroidUtil import AndroidUtil
# from org.allbinary.game.configuration.feature.GraphicsFeatureFactory import GraphicsFeatureFactory
# from org.allbinary.logic.string.StringUtil import StringUtil


def _UnitGameResources_ICON_BUILD() -> object:
    return "_icon" + str(UnitGameResources.BUILD)

lazy_static(UnitGameResources, "ICON_BUILD", _UnitGameResources_ICON_BUILD)

