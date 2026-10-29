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
# package org.allbinary.game.score

from __future__ import annotations

from org.allbinary.graphics.color.ColorChangeListener import ColorChangeListener
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.Paintable import Paintable


class HighScoresPaintable(Paintable, ColorChangeListener, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.basicColor: BasicColor = BasicColorFactory.getInstance().WHITE
        self.highScores: HighScores = NullHighScoresSingletonFactory.getInstance()
        self.anchor: int = Anchor.TOP_LEFT
        self.charHeight: int = 0
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.charHeight = font.getHeight()
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        colorChangeEvent: ColorChangeEvent = eventObject
        self.basicColor = colorChangeEvent.getBasicColorP()
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        width: int = self.displayInfoSingleton.getLastWidth()
        height: int = self.displayInfoSingleton.getLastHeight()
        graphics.setColor(int(self.getBasicColorP()))
        heading: str = self.highScores.getHeading()
        topScoresWidth: int = (graphics.getFont().stringWidth(heading) >> 1)
        charHeight: int = self.charHeight
        graphics.drawString(heading, (width >> 1) - topScoresWidth, charHeight, self.anchor)
        graphics.drawString(self.highScores.getColumnOneHeading(), 10, charHeight * 3, self.anchor)
        columnTwoHeading: str = self.highScores.getColumnTwoHeading()
        columnTwoHeadingWidth: int = graphics.getFont().stringWidth(columnTwoHeading)
        graphics.drawString(columnTwoHeading, width - 10 - columnTwoHeadingWidth, charHeight * 3, self.anchor)
        index: int = 4
        largestSecondColumnWidth: int = columnTwoHeadingWidth
        list_: BasicArrayList = self.highScores.getList()
        size: int = list_.size()
        vectorIndex: int = 0
        highScore: HighScore = None
        while vectorIndex < size and charHeight * index < height - (charHeight * 2):
            highScore = list_.objectArray[vectorIndex]
            nextScoreWidth: int = graphics.getFont().stringWidth(highScore.getScoreString())
            if nextScoreWidth > largestSecondColumnWidth:
                largestSecondColumnWidth = nextScoreWidth
            vectorIndex += 1
        vectorIndex = 0
        while vectorIndex < size and charHeight * index < height - (charHeight * 2):
            highScore = list_.objectArray[vectorIndex]
            graphics.drawString(highScore.getName(), 10, charHeight * index, self.anchor)
            graphics.drawString(highScore.getScoreString(), width - 10 - largestSecondColumnWidth, charHeight * index, self.anchor)
            index += 1
            vectorIndex += 1
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        self.basicColor = basicColor
    

    def getBasicColorP(self) -> BasicColor:
        return self.basicColor
    

    def setHighScores(self, highScores: HighScores) -> None:
        self.highScores = highScores
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.color.ColorChangeEvent import ColorChangeEvent
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.game.score.NullHighScoresSingletonFactory import NullHighScoresSingletonFactory


