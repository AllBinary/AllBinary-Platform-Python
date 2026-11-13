# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.layer.SpriteFactoryInterface import SpriteFactoryInterface


class SpriteFactory(SpriteFactoryInterface):
    instance: SpriteFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> SpriteFactory:
        return SpriteFactory.instance
    

    def createSprite(self, image: Image, frameWidth: int, frameHeight: int) -> Sprite:
        from javax.microedition.lcdui.Image import Image
        from javax.microedition.lcdui.game.Sprite import Sprite
        return Sprite(image, frameWidth, frameHeight)
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
# from org.allbinary.logic.communication.log.LogUtil import LogUtil


def _SpriteFactory_instance() -> object:
    return SpriteFactory()

lazy_static(SpriteFactory, "instance", _SpriteFactory_instance)

