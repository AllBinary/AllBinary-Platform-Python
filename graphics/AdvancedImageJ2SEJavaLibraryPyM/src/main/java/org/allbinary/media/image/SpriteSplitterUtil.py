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
# package org.allbinary.media.image

from __future__ import annotations



class SpriteSplitterUtil:
    instance: SpriteSplitterUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.ANIMATIONS_LABELS: list[str] = ["Row Total:", "Column Total:", "Column Total:", "Row Total:", "Column Total:", "Row Total:"]
        self.DIRECTIONAL_ANIMATIONS: str = "Directional DLRU"
        self.HORIZONTAL_ANIMATIONS: str = "Horizontal Animations"
        self.HORIZONTAL_SPRITE: str = "Horizontal A=R=Y F=C=X"
        self.ROW_NAME: list[str] = ["idle", "walk", "attack", "defeat"]
        self._ROW: str = "_row"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> SpriteSplitterUtil:
        return SpriteSplitterUtil.instance
    

    # throws Exception
    def process(self, imageProcessorInput: ImageProcessorInput, totalFrames: int, totalAnimations: int, widthReduction: int, heightReduction: int, increaseWidth: int, increaseHeight: int, spriteType: str, visitor: ImageProcessedVisitor) -> None:
        from org.allbinary.media.image.ImageUtil import ImageUtil
        from org.allbinary.media.image.ImageUnifierProperties import ImageUnifierProperties
        from org.allbinary.media.image.ImageUnifierCell import ImageUnifierCell
        from org.allbinary.media.image.ImageUnifierUtil import ImageUnifierUtil
        from org.allbinary.media.image.ImageUtil import ImageUtil
        from org.allbinary.media.image.ImageUnifierProperties import ImageUnifierProperties
        from org.allbinary.media.image.ImageUnifierCell import ImageUnifierCell
        from org.allbinary.media.image.ImageUnifierUtil import ImageUnifierUtil
        bufferedImage: BufferedImage = None
        generatedBufferedImageArray: list[list[BufferedImage]] = None
        bufferedImageArray: list[BufferedImage] = imageProcessorInput.getBufferedImageArray()
        for index in range(0, len(bufferedImageArray)):
            bufferedImage = bufferedImageArray[index]
            self.logUtil.putF(spriteType, self, self.commonStrings.RUN)
            if spriteType == self.HORIZONTAL_SPRITE:
                cellHeight: int = bufferedImage.getHeight() / totalAnimations
                cellWidth: int = bufferedImage.getWidth() / totalFrames
                columns: int = totalFrames
                rows: int = totalAnimations
                generatedBufferedImageArray = [[None] * (columns) for _ in range(rows)]
                self.logUtil.putF("Processing Individual Cells columns: " + str(columns) + " rows: " + str(rows), self, self.commonStrings.RUN)
                self.logUtil.putF("Processing Individual Cells cellHeight: " + str(cellHeight) + " cellWidth: " + str(cellWidth), self, self.commonStrings.RUN)
                imageUtil: ImageUtil = ImageUtil.getInstance()
                nameEnding: str = None
                x: int = 0
                y: int = 0
                for index2 in range(0, rows):
                    y = cellHeight * index2
                    for index3 in range(0, columns):
                        x = cellWidth * index3
                        generatedBufferedImageArray[index2][index3] = bufferedImage.getSubimage(x + widthReduction, y + heightReduction, cellWidth - (widthReduction * 2), cellHeight - (heightReduction * 2))
                        if increaseWidth != 0 or increaseHeight != 0:
                            generatedBufferedImageArray[index2][index3] = imageUtil.createBufferedImageAllowTranslate(generatedBufferedImageArray[index2][index3], cellWidth + increaseWidth, cellHeight + increaseHeight, False, True)
                        nameEnding = str(StringMaker().appendint(index2).append(self.commonSeps.UNDERSCORE).appendint(index3))
                        visitor.visit(generatedBufferedImageArray[index2][index3], nameEnding, index)
                self.logUtil.putF("Processing Rows from Cells", self, self.commonStrings.RUN)
                imageUnifierProperties: ImageUnifierProperties = ImageUnifierProperties()
                imageUnifierProperties.setRows(str(1))
                imageUnifierProperties.setColumns(str(columns))
                imageUnifierCell: ImageUnifierCell = ImageUnifierCell(str(cellWidth - (2 * widthReduction)), str(cellHeight - (2 * heightReduction)))
                imageUnifierProperties.setImageUnifierCell(imageUnifierCell)
                for index2 in range(0, rows):
                    y = cellHeight * index2
                    tempBufferedImageArray: list[BufferedImage] = [None] * (columns)
                    for index3 in range(0, columns):
                        tempBufferedImageArray[index3] = generatedBufferedImageArray[index2][index3]
                        nameEnding = str(StringMaker().appendint(index2).append(self.commonSeps.UNDERSCORE).appendint(1).append(self._ROW))
                    generatedBufferedImage: BufferedImage = ImageUnifierUtil.getInstance().getImage(tempBufferedImageArray, imageUnifierProperties)
                    visitor.visit(generatedBufferedImage, nameEnding, index)
            elif spriteType == self.HORIZONTAL_ANIMATIONS:
                pass
            elif spriteType == self.DIRECTIONAL_ANIMATIONS:
                totalFrames2: int = 4
                cellHeight: int = bufferedImage.getHeight() / totalFrames2
                cellWidth: int = bufferedImage.getWidth() / totalAnimations
                columns: int = totalAnimations
                rows: int = totalFrames2
                generatedBufferedImageArray = [[None] * (columns) for _ in range(rows)]
                self.logUtil.putF("Processing Individual Cells for each Direction", self, self.commonStrings.RUN)
                nameEnding: str = None
                x: int = 0
                y: int = 0
                for index2 in range(0, rows):
                    y = cellHeight * index2
                    for index3 in range(0, columns):
                        x = cellWidth * index3
                        generatedBufferedImageArray[index2][index3] = bufferedImage.getSubimage(x + widthReduction, y + heightReduction, cellWidth - (widthReduction * 2), cellHeight - (heightReduction * 2))
                        if increaseWidth != 0 or increaseHeight != 0:
                            generatedBufferedImageArray[index2][index3] = ImageUtil.getInstance().createBufferedImageAllowTranslate(generatedBufferedImageArray[index2][index3], cellWidth + increaseWidth, cellHeight + increaseHeight, False, True)
                        nameEnding = str(StringMaker().append(self.commonStrings.DIRECTION_NAME[index2]).append(self.commonSeps.UNDERSCORE).appendint(index3))
                        visitor.visit(generatedBufferedImageArray[index2][index3], nameEnding, index)
                imageUnifierProperties: ImageUnifierProperties = ImageUnifierProperties()
                imageUnifierProperties.setRows(str(1))
                imageUnifierProperties.setColumns(str(columns))
                imageUnifierCell: ImageUnifierCell = ImageUnifierCell(str(cellWidth - (2 * widthReduction)) + increaseWidth, str(cellHeight - (2 * heightReduction) + increaseHeight))
                imageUnifierProperties.setImageUnifierCell(imageUnifierCell)
                self.logUtil.putF("Processing Rows from Cells for each Direction", self, self.commonStrings.RUN)
                for index2 in range(0, rows):
                    y = cellHeight * index2
                    tempBufferedImageArray: list[BufferedImage] = [None] * (columns)
                    for index3 in range(0, columns):
                        tempBufferedImageArray[index3] = generatedBufferedImageArray[index2][index3]
                        nameEnding = str(StringMaker().append(self.commonStrings.DIRECTION_NAME[index2]).append(self.commonSeps.UNDERSCORE).appendint(1).append(self._ROW))
                    generatedBufferedImage: BufferedImage = ImageUnifierUtil.getInstance().getImage(tempBufferedImageArray, imageUnifierProperties)
                    visitor.visit(generatedBufferedImage, nameEnding, index)
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


SpriteSplitterUtil.instance = SpriteSplitterUtil()

