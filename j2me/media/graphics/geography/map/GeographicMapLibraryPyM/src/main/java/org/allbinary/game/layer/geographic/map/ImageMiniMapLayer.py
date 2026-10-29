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
# package org.allbinary.game.layer.geographic.map

from __future__ import annotations

from org.allbinary.game.layer.geographic.map.MiniMapLayer import MiniMapLayer


class ImageMiniMapLayer(MiniMapLayer):

    def _init_fields(self) -> None:
        self.image: Image = NullImage.NULL_IMAGE
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, geographicMapInterface: BasicGeographicMap, viewPosition: ViewPositionBase) -> None:
        super().__init__(geographicMapInterface, viewPosition)
        self._init_fields()
    

    # throws Exception
    def init(self) -> None:
        aWidth: int = self.allBinaryTiledLayer.getWidth()
        aHeight: int = self.allBinaryTiledLayer.getHeight()
        self.image = PaintableToImageUtil.getImage(self.allBinaryTiledLayer, aWidth, aHeight)
    

    def paint(self, graphics: Graphics) -> None:
        graphics.drawImage(self.image, self.x, self.y, self.anchor)
        self.paintDots(graphics)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.image.PaintableToImageUtil import PaintableToImageUtil
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.view.ViewPositionBase import ViewPositionBase


