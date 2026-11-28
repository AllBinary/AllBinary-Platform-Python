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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.paint.ProcessPaintable import ProcessPaintable


@java_inherited_overloads
class BufferedGameCanvasPaintHelper(ProcessPaintable):
    MAX_IMAGES: int = 4
    def _java_defaults(self):
        vars(self).setdefault("gameCanvas", None)
        vars(self).setdefault("offScreenImage", None)
        vars(self).setdefault("previousImage", None)
        vars(self).setdefault("circularIndexUtil", None)
        vars(self).setdefault("drawCircularIndexUtil", None)
        vars(self).setdefault("anchor", 0)

    def _init_fields(self) -> None:
        from javax.microedition.lcdui.Image import Image
        from javax.microedition.lcdui.NullCanvas import NullCanvas
        from javax.microedition.lcdui.NullImage import NullImage
        from org.allbinary.graphics.Anchor import Anchor
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        self.gameCanvas: Canvas = NullCanvas.NULL_CANVAS
        self.offScreenImage: list[Image] = [None] * (BufferedGameCanvasPaintHelper.MAX_IMAGES)
        self.previousImage: Image = NullImage.NULL_IMAGE
        self.circularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstance(BufferedGameCanvasPaintHelper.MAX_IMAGES)
        self.drawCircularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstanceAt(BufferedGameCanvasPaintHelper.MAX_IMAGES - 1, BufferedGameCanvasPaintHelper.MAX_IMAGES)
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, gameCanvas: AllBinaryGameCanvas) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        raise Exception("No Longer Used")
    

    def process(self) -> None:
        from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
        myCanvas: MyCanvas = (self.gameCanvas)
        myCanvas.draw(self.offScreenImage[self.circularIndexUtil.getIndex()].getGraphics())
        self.circularIndexUtil.next()
        self.drawCircularIndexUtil.next()
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.previousImage = self.offScreenImage[self.drawCircularIndexUtil.getIndex()]
        graphics.drawImage(self.previousImage, 0, 0, self.anchor)
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullCanvas import NullCanvas
# from javax.microedition.lcdui.NullImage import NullImage
# from org.allbinary.graphics.Anchor import Anchor
# from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
# from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


