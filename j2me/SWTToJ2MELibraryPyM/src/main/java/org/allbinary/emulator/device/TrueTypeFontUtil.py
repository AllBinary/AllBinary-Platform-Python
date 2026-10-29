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
# package org.allbinary.emulator.device

from __future__ import annotations

from org.allbinary.emulator.device.TrueTypeFontUtilBase import TrueTypeFontUtilBase


#TTF
class TrueTypeFontUtil(TrueTypeFontUtilBase):
    instance: TrueTypeFontUtil = None

    def _init_fields(self) -> None:
        self.preResourceImageUtil: PreResourceImageUtil = PreResourceImageUtil.getInstance()
        self.widthFloatArray: list[float] = None
        self.fontImage: OpenGLESImage = OpenGLESImage.NULL_OPENGL_IMAGE
        self.widthScale: float = None
    

    @staticmethod
    def getInstance() -> TrueTypeFontUtil:
        return TrueTypeFontUtil.instance
    

    def __init__(self) -> None:
        super().__init__(2)
        self._init_fields()
        if AvianUtil.isAvian():
            self.widthFloatArray = [1504.0, 967.0, 527.0, 961.0, 957.0, 1087.0, 920.0, 954.0, 973.0, 961.0, 955.0, 1296.0, 1013.0, 1106.0, 1167.0, 815.0, 815.0, 1216.0, 1110.0, 170.0, 520.0, 1056.0, 815.0, 1448.0, 1142.0, 1345.0, 927.0, 1345.0, 1030.0, 920.0, 1096.0, 1119.0, 1219.0, 1841.0, 1166.0, 1147.0, 1005.0, 879.0, 965.0, 792.0, 964.0, 927.0, 753.0, 1034.0, 916.0, 196.0, 469.0, 877.0, 166.0, 1563.0, 916.0, 1007.0, 965.0, 964.0, 631.0, 777.0, 649.0, 917.0, 1026.0, 1548.0, 993.0, 1028.0, 795.0, 241.0, 798.0, 241.0, 905.0, 1477.0, 393.0, 961.0, 961.0, 961.0, 961.0, 555.0, 1029.0, 1010.0, 1378.0, 952.0, 952.0, 952.0, 952.0, 463.0, 463.0, 926.0, 961.0, 491.0, 930.0, 457.0, 457.0, 644.0, 643.0, 326.0, 186.0, 1219.0, 241.0, 1599.0, 961.0, 302.0, 711.0, 961.0, 961.0, 710.0, 141.0, 1504.0, 1504.0, 1504.0, 1504.0, 1504.0, 1504.0, 1504.0, 1504.0]
        else:
            self.widthFloatArray = [1504.0, 967.0, 527.0, 961.0, 957.0, 1087.0, 920.0, 954.0, 973.0, 961.0, 955.0, 1296.0, 1013.0, 1106.0, 1167.0, 815.0, 815.0, 1216.0, 1110.0, 170.0, 520.0, 1056.0, 815.0, 1448.0, 1142.0, 1345.0, 927.0, 1345.0, 1030.0, 920.0, 1096.0, 1119.0, 1219.0, 1841.0, 1166.0, 1147.0, 1005.0, 879.0, 965.0, 792.0, 964.0, 927.0, 753.0, 1034.0, 916.0, 196.0, 469.0, 877.0, 166.0, 1563.0, 916.0, 1007.0, 965.0, 964.0, 631.0, 777.0, 649.0, 917.0, 1026.0, 1548.0, 993.0, 1028.0, 795.0, 241.0, 798.0, 241.0, 905.0, 1477.0, 393.0, 961.0, 555.0, 1029.0, 1010.0, 1378.0, 952.0, 463.0, 463.0, 926.0, 961.0, 491.0, 930.0, 457.0, 457.0, 644.0, 643.0, 326.0, 186.0, 1219.0, 241.0, 1599.0, 961.0, 302.0, 711.0, 961.0, 961.0, 710.0, 141.0, 1504.0, 1504.0]
        self.widthScale = (1.2 if (self.scale == 2) else 1.0)
    

    def getFontBitmapGL(self, gl: GL10, filename: str, cellSize: int, basicColor: BasicColor) -> Image:
        try:
            if self.fontImage == OpenGLESImage.NULL_OPENGL_IMAGE:
                canvasStrings: CanvasStrings = CanvasStrings.getInstance()
                openGLCapabilities: OpenGLCapabilities = OpenGLCapabilities.getInstance()
                if openGLCapabilities.isTextureSizeValid(1024) and self.scale == 2:
                    FONT_ATLAS_1024: str = "/font_1024.png"
                    image: Image = Image.createImage(ResourceUtil.getInstance().getResourceAsStream(FONT_ATLAS_1024))
                    image.setName(canvasStrings.FONT_ATLAS)
                    self.fontImage = self.preResourceImageUtil.encapsulate(image)
                elif openGLCapabilities.isTextureSizeValid(512):
                    FONT_ATLAS_512: str = "/font_512.png"
                    image: Image = Image.createImage(ResourceUtil.getInstance().getResourceAsStream(FONT_ATLAS_512))
                    image.setName(canvasStrings.FONT_ATLAS)
                    self.fontImage = self.preResourceImageUtil.encapsulate(image)
                else:
                    FONT_ATLAS_512: str = "/font_512.png"
                    image: Image = Image.createImage(ResourceUtil.getInstance().getResourceAsStream(FONT_ATLAS_512))
                    image.setName(canvasStrings.FONT_ATLAS)
                    self.fontImage = self.preResourceImageUtil.encapsulate(image)
                return self.fontImage
            else:
                return self.fontImage
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.putOE(commonStrings.EXCEPTION, self, commonStrings.EXCEPTION, e)
            raise RuntimeError()
    

    def saveFontAtlasAsFile(self) -> None:
        image: Image = self.getFontBitmap(None, self.cellSize, BasicColorFactory.getInstance().WHITE)
        imageLoader: ImageLoader = ImageLoader()
        imageData: ImageData = (image).image.getImageData()
        imageData.transparentPixel = imageData.getPixel(0, 0)
        imageLoader.data = [imageData]
        imageLoader.save(CommonSeps.getInstance().PERIOD + CanvasStrings.getInstance().FONT_ATLAS, SWT.IMAGE_PNG)
    

    def getFontBitmap(self, filename: str, cellSize: int, basicColor: BasicColor) -> Image:
        cellsPerRow2: int = self.CELLS_PER_ROW * 2
        cellsPerRow3: int = self.CELLS_PER_ROW * 3
        cellsPerRow4: int = self.CELLS_PER_ROW * 4
        cellsPerRow5: int = self.CELLS_PER_ROW * 5
        cellsPerRow6: int = self.CELLS_PER_ROW * 6
        cellsPerRow7: int = self.CELLS_PER_ROW * 7
        image: Image = Image.createImage(self.textureSize, self.textureSize)
        graphics: Graphics = image.getGraphics()
        graphics.setColor(int(basicColor))
        biggestHeight: int = 0
        bounds: Rectangle = Rectangle(PointFactory.getInstance().createXY(0, 0), cellSize, cellSize)
        x: int = 0
        y: int = 0
        for index in range(0, self.size):
            self.characterArray[0] = self.pattern.charAt(index)
            self._characterWidth[index] = bounds.getMaxX()
            if bounds.getMaxY() - bounds.getPoint().getX() > biggestHeight:
                biggestHeight = bounds.getMaxY() - bounds.getPoint().getX()
            x = (index % self.CELLS_PER_ROW) * cellSize
            x += (cellSize >> 1)
            x -= (self._characterWidth[index] >> 1)
            y = -(cellSize >> 1)
            if index >= self.CELLS_PER_ROW:
                y += cellSize
            if index >= cellsPerRow2:
                y += cellSize
            if index >= cellsPerRow3:
                y += cellSize
            if index >= cellsPerRow4:
                y += cellSize
            if index >= cellsPerRow5:
                y += cellSize
            if index >= cellsPerRow6:
                y += cellSize
            if index >= cellsPerRow7:
                y += cellSize
            y += cellSize
            y -= (cellSize >> 2)
            graphics.drawChar(self.characterArray[0], x, y, 0)
        return image
    

    def getFontWidths(self, filename: str, fontSize: int) -> list[int]:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        for index in range(0, self.size):
            self.characterArray[0] = self.pattern.charAt(index)
            if self.characterArray[0] == ' ':
                self._characterWidth[index] = (int(fontSize / 4))
            else:
                shortPatternIndex: int = self.shortPattern.indexOf(self.characterArray[0])
                w: int = int((self.widthFloatArray[shortPatternIndex] / 75.0)) + 19
                self._characterWidth[index] = w
                if self.characterArray[0] == '.' or self.characterArray[0] == '1':
                    self._characterWidth[index] += 4
                if self.characterArray[0] >= 'a' and self.characterArray[0] < 'k':
                    self._characterWidth[index] -= 2
                if self.characterArray[0] >= 'k' and self.characterArray[0] < 'v':
                    self._characterWidth[index] -= 4
                if self.characterArray[0] >= 'v' and self.characterArray[0] < 'z':
                    self._characterWidth[index] -= 8
                if self.characterArray[0] == 'D':
                    self._characterWidth[index] -= 4
                if self.characterArray[0] >= 'A' and self.characterArray[0] <= 'Z':
                    self._characterWidth[index] -= 2
            self._characterWidth[index] *= self.widthScale
        return self._characterWidth
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.eclipse.swt.SWT import SWT
from org.eclipse.swt.graphics.ImageData import ImageData
from org.eclipse.swt.graphics.ImageLoader import ImageLoader
from org.microemu.device.swt.SwtMutableImage import SwtMutableImage
from org.allbinary.AvianUtil import AvianUtil
from org.allbinary.data.resource.ResourceUtil import ResourceUtil
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.graphics.opengles.OpenGLCapabilities import OpenGLCapabilities
from org.allbinary.image.PreResourceImageUtil import PreResourceImageUtil
from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


TrueTypeFontUtil.instance = TrueTypeFontUtil()

