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
# package org.allbinary.game.layer.hud.basic

from __future__ import annotations

from org.allbinary.game.layer.hud.basic.HealthGraphic import HealthGraphic


class ImageHealthGraphic(HealthGraphic):

    def _init_fields(self) -> None:
        self.image: list[Image] = None
    

    def __init__(self, animationInterface: AnimationInterface, healthInterface: HealthInterface, location: int, direction: int) -> None:
        super().__init__(animationInterface, healthInterface, location, direction)
        self._init_fields()
        self.image = [None] * (self.healthInterface.getMaxHealth())
        imageCacheFactory: ImageCacheFactory = ImageCacheFactory.getInstance()
        for numOfHealth in range(0, self.max + 1):
            self.image[numOfHealth] = imageCacheFactory.get(self, numOfHealth + 1 * 10, 10)
        for numOfHealth in range(0, self.max + 1):
            for index in range(0, numOfHealth):
                self.animationInterface.paint(self.image[numOfHealth].getGraphics(), numOfHealth * 10, 0)
    

    def paint(self, graphics: Graphics) -> None:
        graphics.drawImage(self.image[self.max], self.x, self.y, Anchor.TOP_LEFT)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.AnimationInterface import AnimationInterface
from org.allbinary.game.health.HealthInterface import HealthInterface
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.image.ImageCacheFactory import ImageCacheFactory


