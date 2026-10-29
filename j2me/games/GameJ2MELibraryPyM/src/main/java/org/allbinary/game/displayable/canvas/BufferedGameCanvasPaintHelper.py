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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from org.allbinary.graphics.paint.ProcessPaintable import ProcessPaintable


class BufferedGameCanvasPaintHelper(ProcessPaintable):
    MAX_IMAGES: int = 4

    def _init_fields(self) -> None:
        self.gameCanvas: Canvas = NullCanvas.NULL_CANVAS
        self.offScreenImage: list[Image] = [None] * (BufferedGameCanvasPaintHelper.MAX_IMAGES)
        self.previousImage: Image = NullImage.NULL_IMAGE
        self.circularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstance(BufferedGameCanvasPaintHelper.MAX_IMAGES)
        self.drawCircularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstanceAt(BufferedGameCanvasPaintHelper.MAX_IMAGES - 1, BufferedGameCanvasPaintHelper.MAX_IMAGES)
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, gameCanvas: AllBinaryGameCanvas) -> None:
        super().__init__()
        self._init_fields()
        raise Exception("No Longer Used")
    

    def process(self) -> None:
        myCanvas: MyCanvas = (self.gameCanvas)
        myCanvas.draw(self.offScreenImage[self.circularIndexUtil.getIndex()].getGraphics())
        self.circularIndexUtil.next()
        self.drawCircularIndexUtil.next()
    

    def paint(self, graphics: Graphics) -> None:
        self.previousImage = self.offScreenImage[self.drawCircularIndexUtil.getIndex()]
        graphics.drawImage(self.previousImage, 0, 0, self.anchor)
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullCanvas import NullCanvas
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


