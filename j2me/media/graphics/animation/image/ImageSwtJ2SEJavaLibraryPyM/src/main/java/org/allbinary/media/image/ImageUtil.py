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
# package org.allbinary.media.image

from __future__ import annotations



class ImageUtil:
    instance: ImageUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.IIOIMAGE_POOL_NAME: str = "IIOIMAGE_POOL_NAME"
        self.CREATE_BUFFERED_IMAGE: str = "createBufferedImage"
    

    @staticmethod
    def getInstance() -> ImageUtil:
        return ImageUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
    

    def create(self, width: int, height: int) -> Image:
        from org.allbinary.media.image.Image import Image
        display: Display = BareMain.shell.getDisplay()
        return Image(display, width, height)
    

    # throws Exception
    def createBufferedImage(self, bufferedImageArray: list[Image], percent: int, scale: bool) -> list[Image]:
        size: int = len(bufferedImageArray)
        scaledBufferedImageArray: list[Image] = [None] * (size)
        bufferedImage: Image = None
        imageData: ImageData = None
        for index in range(0, size):
            bufferedImage = bufferedImageArray[index]
            imageData = bufferedImage.getImageData()
            newWidth: int = int((imageData.width * percent / 100))
            newHeight: int = int((imageData.height * percent / 100))
            scaledBufferedImageArray[index] = self.createBufferedImage5(bufferedImage, newWidth, newHeight, scale)
        return scaledBufferedImageArray
    

    # throws Exception
    def createBufferedImage2(self, bufferedImageArray: list[Image], percent: float, scale: bool) -> list[Image]:
        size: int = len(bufferedImageArray)
        scaledBufferedImageArray: list[Image] = [None] * (size)
        bufferedImage: Image = None
        imageData: ImageData = None
        for index in range(0, size):
            bufferedImage = bufferedImageArray[index]
            imageData = bufferedImage.getImageData()
            newWidth: int = int((imageData.width * percent))
            newHeight: int = int((imageData.height * percent))
            scaledBufferedImageArray[index] = self.createBufferedImage5(bufferedImage, newWidth, newHeight, scale)
        return scaledBufferedImageArray
    

    # throws Exception
    def createBufferedImage3(self, bufferedImageArray: list[Image], width: int, height: int, scale: bool) -> list[Image]:
        size: int = len(bufferedImageArray)
        scaledBufferedImageArray: list[Image] = [None] * (size)
        for index in range(0, size):
            scaledBufferedImageArray[index] = self.createBufferedImage5(bufferedImageArray[index], width, height, scale)
        return scaledBufferedImageArray
    

    # throws Exception
    def createBufferedImage4(self, bufferedImage: Image, newWidth: int, newHeight: int) -> Image:
        return self.createBufferedImage5(bufferedImage, newWidth, newHeight, True)
    

    # throws Exception
    def createBufferedImage5(self, bufferedImage: Image, newWidth: int, newHeight: int, scale: bool) -> Image:
        return self.createBufferedImage6(bufferedImage, newWidth, newHeight, scale, False)
    

    # throws Exception
    def createBufferedImage6(self, bufferedImage: Image, newWidth: int, newHeight: int, scale: bool, allowTranslate: bool) -> Image:
        from org.allbinary.media.image.Image import Image
        imageData: ImageData = bufferedImage.getImageData()
        width: float = imageData.width
        height: float = imageData.height
        d_newWidth: float = float(newWidth)
        d_newHeight: float = float(newHeight)
        widthRatio: float = d_newWidth / width
        heightRatio: float = d_newHeight / height
        ratioX: float = 1.0
        ratioY: float = 1.0
        if scale:
            ratioX = widthRatio
            ratioY = heightRatio
        self.logUtil.putF(str(StringMaker().appendfloat(width).append(self.commonSeps.FORWARD_SLASH).appendfloat(height).append(self.commonSeps.COLON).appendint(newWidth).append(self.commonSeps.FORWARD_SLASH).appendint(newHeight).append(self.commonSeps.COLON).appendfloat(widthRatio).append(self.commonSeps.FORWARD_SLASH).appendfloat(heightRatio)), self, self.CREATE_BUFFERED_IMAGE)
        dx: float = 0.0
        dy: float = 0.0
        if not scale and allowTranslate:
            dx = (float(newWidth) - width) / 2.0
            dy = (float(newHeight) - height) / 2.0
            self.logUtil.putF(str(StringMaker().append("Translate dx: ").appendfloat(dx).append(" dy: ").appendfloat(dy)), self, self.CREATE_BUFFERED_IMAGE)
        newBufferedImage: Image = Image(BareMain.shell.getDisplay(), newWidth, newHeight)
        gc: GC = GC(newBufferedImage)
        affineTransform: Transform = Transform(gc.getDevice())
        affineTransform.scale(ratioX, ratioY)
        affineTransform.translate(dx, dy)
        gc.setTransform(affineTransform)
        gc.setAntialias(SWT.ON)
        gc.setInterpolation(SWT.HIGH)
        gc.drawImage(bufferedImage, 0, 0, bufferedImage.getBounds().width, bufferedImage.getBounds().height, 0, 0, newWidth, newHeight)
        gc.dispose()
        return newBufferedImage
    

    def drawTransformedImage(self, image: Image, parent: Composite, dx: int, dy: int, width: int, height: int) -> Canvas:
        imageCanvas: Canvas = Canvas(parent, SWT.NONE)
        imageCanvas.addPaintListener((PaintListener()  # Java anonymous class body:
#             
# 
#             def paintControl(self, event: PaintEvent) -> None:
#                 gc: GC = event.gc
#                 affineTransform: Transform = Transform(gc.getDevice())
#                 affineTransform.translate(dx, dy)
#                 gc.setAntialias(SWT.ON)
#                 gc.setInterpolation(SWT.HIGH)
#                 gc.drawImage(image, 0, 0, image.getBounds().width, image.getBounds().height, 0, 0, width, height)
))
        return imageCanvas
    

    def toString(self, bufferedImage: Image) -> str:
        commonLabels: CommonLabels = CommonLabels.getInstance()
        stringBuffer: StringMaker = StringMaker()
        imageData: ImageData = bufferedImage.getImageData()
        stringBuffer.append(" org.eclipse.swt.graphics.Image: ")
        stringBuffer.append(commonLabels.WIDTH_LABEL)
        stringBuffer.appendint(int(imageData.width))
        stringBuffer.append(commonLabels.HEIGHT_LABEL)
        stringBuffer.appendint(int(imageData.height))
        stringBuffer.append(" Type: ")
        stringBuffer.appendint(int(imageData.type_))
        return str(stringBuffer)
from org.eclipse.swt.SWT import SWT
from org.eclipse.swt.widgets.Canvas import Canvas
from org.eclipse.swt.widgets.Composite import Composite
from org.eclipse.swt.graphics.GC import GC
from org.eclipse.swt.graphics.ImageData import ImageData
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.eclipse.swt.events.PaintEvent import PaintEvent
from org.eclipse.swt.events.PaintListener import PaintListener
from org.eclipse.swt.graphics.Transform import Transform
from org.eclipse.swt.widgets.Display import Display
from org.microemu.app.BareMain import BareMain


ImageUtil.instance = ImageUtil()

