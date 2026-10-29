# Generated Code Do Not Modify
# package org.allbinary.media.image

from __future__ import annotations



class BufferedImageUtil2:
    instance: BufferedImageUtil2 = None

    def _init_fields(self) -> None:
        self.imageUtil: ImageUtil = ImageUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BufferedImageUtil2:
        return BufferedImageUtil2.instance
    

    def createSpriteImage(self, bufferedImageArray: list[BufferedImage]) -> BufferedImage:
        columns: int = len(bufferedImageArray)
        max: int = columns
        rows: int = 0
        if len(bufferedImageArray) < columns:
            columns = len(bufferedImageArray)
        rows = (int(len(bufferedImageArray) / columns))
        if len(bufferedImageArray) % columns != 0:
            rows += 1
        bufferedImage: BufferedImage = self.imageUtil.create(bufferedImageArray[0].getWidth(None) * columns, bufferedImageArray[0].getHeight(None) * rows)
        g: Graphics2D = bufferedImage.createGraphics()
        columnIndex: int = 0
        rowIndex: int = 0
        for index in range(0, len(bufferedImageArray)):
            if int(index / max) != 0 and index % max == 0:
                rowIndex += 1
                columnIndex = 0
            g.drawImage(bufferedImageArray[index], bufferedImageArray[index].getWidth(None) * columnIndex, bufferedImageArray[index].getHeight(None) * rowIndex, bufferedImageArray[index].getWidth(None), bufferedImageArray[index].getHeight(None), None)
            columnIndex += 1
        g.dispose()
        return bufferedImage
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.media.image.ImageUtil import ImageUtil


BufferedImageUtil2.instance = BufferedImageUtil2()

