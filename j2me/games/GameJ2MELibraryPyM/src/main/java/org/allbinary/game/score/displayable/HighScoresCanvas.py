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
# package org.allbinary.game.score.displayable

from __future__ import annotations

import time
from org.allbinary.game.displayable.canvas.GameCommandCanvas import GameCommandCanvas
from org.allbinary.game.score.HighScoresResultsListener import HighScoresResultsListener


class HighScoresCanvas(GameCommandCanvas, HighScoresResultsListener):
    NAME: str = "HighScoresCanvas"

    def _init_fields(self) -> None:
        self.paintable: Paintable = NullPaintable.getInstance()
        self.highScoreCommandsFactory: HighScoreCommandsFactory = HighScoreCommandsFactory.getInstance()
        self.waitPaintable: SimpleTextPaintable = SimpleTextPaintable(self.commonStrings.PLEASE_WAIT_FOR_SERVER, BasicColorFactory.getInstance().WHITE)
        self.highScoresPaintable: HighScoresPaintable = None
        self.highScoresFactoryInterface: HighScoresFactoryInterface = None
        self.colorFillPaintable: ColorFillBasePaintable = None
        self.highScoresHelper: HighScoresHelperBase = HighScoresHelperBase()
        self.gameInfo: GameInfo = None
        self.highScoresCanvasInputProcessor: HighScoresCanvasInputProcessor = None
        self.currentCommand: Command = self.highScoreCommandsFactory.HIGH_SCORE_COMMANDS[0]
        self.hasPainted: bool = False
    

    def __init__(self, commandListener: CommandListener, allBinaryGameLayerManager: AllBinaryGameLayerManager, gameInfo: GameInfo, paintable: HighScoresPaintable, highScoresFactoryInterface: HighScoresFactoryInterface, highScoresCanvasInputProcessorFactoryInterface: HighScoresCanvasInputProcessorFactoryInterface) -> None:
        from org.allbinary.game.score.displayable.HighScoreRunnable import HighScoreRunnable
        super().__init__(commandListener, HighScoresCanvas.NAME, allBinaryGameLayerManager.getBackgroundBasicColor(), allBinaryGameLayerManager.getForegroundBasicColor())
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.highScoresPaintable = paintable
        self.highScoresFactoryInterface = highScoresFactoryInterface
        self.highScoresCanvasInputProcessor = highScoresCanvasInputProcessorFactoryInterface.getInstance(self)
        self.gameInfo = gameInfo
        self.waitPaintable.setBasicColorP(allBinaryGameLayerManager.getForegroundBasicColor())
        self.getHighScoresPaintable().setBasicColorP(allBinaryGameLayerManager.getForegroundBasicColor())
        self.colorFillPaintable = ColorFillPaintableFactory.getInstance().getInstance(allBinaryGameLayerManager.getBackgroundBasicColor(), False)
        if self.highScoresHelper.getHighScoresArray() == NoHighScoresFactory.getInstance().NO_HIGH_SCORES:
            self.setPaintable(self.waitPaintable)
        else:
            self.logUtil.putF("Show HighScores that are already loaded", self, self.commonStrings.CONSTRUCTOR)
            self.updateCommand(self.currentCommand)
            self.setPaintable(self.getHighScoresPaintable())
        class HighScoreRunnable(ARunnable):

            def _init_fields(self) -> None:
                self.highScoresCanvas: HighScoresCanvas = None
            

            def __init__(self, highScoresCanvas: HighScoresCanvas) -> None:
                super().__init__()
                self._init_fields()
                self.highScoresCanvas = highScoresCanvas
            

            def run(self) -> None:
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil: LogUtil = LogUtil.getInstance()
                highScoresCanvas: HighScoresCanvas = self.highScoresCanvas
                try:
                    isHTML: bool = J2MEUtil.isHTML()
                    if not isHTML:
                        while not highScoresCanvas.hasPainted:
                            pass
                        highScoresCanvas.hasPainted = False
                    stringMaker: StringMaker = StringMaker()
                    systemWrapper: ABSystemWrapper = ABSystemWrapper.getInstance()
                    currentTimeMillis: int = systemWrapper.currentTimeMillis()
                    logUtil.putF(str(stringMaker.append("HighScoresCanvas - Request repaint to be sure: ").appendlong(currentTimeMillis)), self, commonStrings.RUN)
                    highScoresCanvas.repaintBehavior.onChangeRepaint(highScoresCanvas)
                    if not isHTML:
                        while not highScoresCanvas.hasPainted:
                            pass
                    stringMaker.delete(0, stringMaker.length())
                    logUtil.putF(str(stringMaker.append("HighScoresCanvas - Now that the canvas has completed repaint go ahead and fetch the scores: ").appendlong(currentTimeMillis)), self, commonStrings.RUN)
                    highScoresCanvas.executeUpdate()
                except Exception as e:
                    logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
        SecondaryThreadPool.getInstance().runTask(HighScoreRunnable(self))
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        self.removeAllCommands()
        self.addCommand(GameCommandsFactory.getInstance().CLOSE_AND_SHOW_GAME_CANVAS)
        self.setCommandListener(cmdListener)
    

    def open(self) -> None:
        super().open()
        self.highScoresCanvasInputProcessor.open()
    

    # throws Exception
    def close(self) -> None:
        super().close()
        self.highScoresCanvasInputProcessor.close()
    

    def paint(self, graphics: Graphics) -> None:
        self.colorFillPaintable.paint(graphics)
        self.paintable.paint(graphics)
        if self.waitPaintable != self.paintable:
            self.highScoresCanvasInputProcessor.paint(graphics)
        super().paint(graphics)
        self.hasPainted = True
    

    def executeUpdate(self) -> None:
        try:
            self.highScoresFactoryInterface.fetchHighScores(self.getGameInfo(), self)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.UPDATE, e)
    

    def getHighScoresPaintable(self) -> HighScoresPaintable:
        return self.highScoresPaintable
    

    def setHighScoresArray(self, highScoresArray: list[HighScores]) -> None:
        try:
            if highScoresArray is not None:
                self.logUtil.putF(str(StringMaker().append(self.commonStrings.START).appendint(len(highScoresArray))), self, "setHighScoresArray")
            else:
                self.logUtil.putF(self.commonStrings.START, self, "setHighScoresArray")
            self.highScoresHelper.setHighScoresArray(highScoresArray)
            self.updateCommand(self.currentCommand)
            self.setPaintable(self.getHighScoresPaintable())
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.UPDATE, e)
    

    # throws Exception
    def updateCommand(self, command: Command) -> None:
        self.logUtil.putF(str(StringMaker().append(self.commonStrings.START).append(self.stringUtil.toString(command))), self, self.commonStrings.UPDATE)
        gameCommandsFactory: GameCommandsFactory = GameCommandsFactory.getInstance()
        if self.highScoreCommandsFactory.isHighScoreCommand(command):
            index: int = self.highScoreCommandsFactory.getIndex(command)
            nextIndex: int = index + 1
            highScoresArray: list[HighScores] = self.highScoresHelper.getHighScoresArray()
            if nextIndex >= len(highScoresArray):
                nextIndex = 0
            if len(highScoresArray) > 0:
                self.getHighScoresPaintable().setHighScores(highScoresArray[index])
            else:
                self.getHighScoresPaintable().setHighScores(NullHighScoresSingletonFactory.getInstance())
            if index != nextIndex:
                self.removeAllCommands()
                self.addCommand(gameCommandsFactory.CLOSE_AND_SHOW_GAME_CANVAS)
                self.addCommand(self.highScoreCommandsFactory.HIGH_SCORE_COMMANDS[nextIndex])
        self.currentCommand = command
        self.close()
        super().initMenu()
        self.open()
        self.repaintBehavior.onChangeRepaint(self)
    

    def getGameInfo(self) -> GameInfo:
        return self.gameInfo
    

    def setPaintable(self, paintable: Paintable) -> None:
        self.paintable = paintable
        self.repaintBehavior.onChangeRepaint(self)
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.paint.ColorFillBasePaintable import ColorFillBasePaintable
from org.allbinary.game.paint.ColorFillPaintableFactory import ColorFillPaintableFactory
from org.allbinary.game.score.HighScoreCommandsFactory import HighScoreCommandsFactory
from org.allbinary.game.score.HighScores import HighScores
from org.allbinary.game.score.HighScoresCanvasInputProcessor import HighScoresCanvasInputProcessor
from org.allbinary.game.score.HighScoresCanvasInputProcessorFactoryInterface import HighScoresCanvasInputProcessorFactoryInterface
from org.allbinary.game.score.HighScoresFactoryInterface import HighScoresFactoryInterface
from org.allbinary.game.score.HighScoresHelperBase import HighScoresHelperBase
from org.allbinary.game.score.HighScoresPaintable import HighScoresPaintable
from org.allbinary.game.score.NoHighScoresFactory import NoHighScoresFactory
from org.allbinary.game.score.NullHighScoresSingletonFactory import NullHighScoresSingletonFactory
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.graphics.paint.SimpleTextPaintable import SimpleTextPaintable
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.thread.ARunnable import ARunnable
from org.allbinary.thread.SecondaryThreadPool import SecondaryThreadPool
from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper


