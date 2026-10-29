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

import threading
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.game.score.HighScoresCanvasInputProcessor import HighScoresCanvasInputProcessor


class HighScoresCanvasLevelChangeInputProcessor(HighScoresCanvasInputProcessor, UpdateMyFontInterface):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.INSTRUCTIONS: str = "(Right = Next Track, Left = Previous Track)"
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.anchor: int = Anchor.TOP_LEFT
        self.fontHeight: int = 0
    

    def __init__(self, highScoresCanvas: HighScoresCanvas) -> None:
        super().__init__(highScoresCanvas)
        self._init_fields()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.fontHeight = font.getHeight()
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def open(self) -> None:
        GameKeyEventHandler.getInstance().addListener(self)
    

    def close(self) -> None:
        GameKeyEventHandler.getInstance().removeListener(self)
    

    def update(self) -> None:
        with self._lock:
            return self._update_unlocked()

    def _update_unlocked(self) -> None:
        list_: BasicArrayList = self.getGameKeyEventList()
        size: int = list_.size()
        for index in range(0, size):
            anyType: object = list_.objectArray[index]
            key: int = GameKeyEventUtil.getKey(anyType)
            if key == Canvas.RIGHT:
                self.getHighScoresCanvas().getGameInfo().nextGameLevel()
            elif key == Canvas.LEFT:
                self.getHighScoresCanvas().getGameInfo().previousGameLevel()
            self.getHighScoresCanvas().executeUpdate()
        list_.clear()
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        width: int = self.displayInfoSingleton.getLastWidth()
        topScoresWidth: int = (graphics.getFont().stringWidth(self.INSTRUCTIONS) >> 1)
        graphics.drawString(self.INSTRUCTIONS, (width >> 1) - topScoresWidth, self.fontHeight * 2, self.anchor)
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.input.event.GameKeyEventHandler import GameKeyEventHandler
from org.allbinary.game.input.event.GameKeyEventUtil import GameKeyEventUtil
from org.allbinary.game.score.displayable.HighScoresCanvas import HighScoresCanvas
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.util.BasicArrayList import BasicArrayList


