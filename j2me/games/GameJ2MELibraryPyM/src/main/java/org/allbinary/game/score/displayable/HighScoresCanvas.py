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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.displayable.canvas.GameCommandCanvas import GameCommandCanvas
from org.allbinary.game.score.HighScoresResultsListener import HighScoresResultsListener


@java_inherited_overloads
class HighScoresCanvas(*java_bases(GameCommandCanvas, HighScoresResultsListener)):
    NAME: str = "HighScoresCanvas"
    def _java_defaults(self):
        vars(self).setdefault("paintable", None)
        vars(self).setdefault("highScoreCommandsFactory", None)
        vars(self).setdefault("waitPaintable", None)
        vars(self).setdefault("highScoresPaintable", None)
        vars(self).setdefault("highScoresFactoryInterface", None)
        vars(self).setdefault("colorFillPaintable", None)
        vars(self).setdefault("highScoresHelper", None)
        vars(self).setdefault("gameInfo", None)
        vars(self).setdefault("highScoresCanvasInputProcessor", None)
        vars(self).setdefault("currentCommand", None)
        vars(self).setdefault("hasPainted", False)

    def _init_fields(self) -> None:
        from org.allbinary.game.score.HighScoreCommandsFactory import HighScoreCommandsFactory
        from org.allbinary.game.score.HighScoresHelperBase import HighScoresHelperBase
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        from org.allbinary.graphics.paint.NullPaintable import NullPaintable
        from org.allbinary.graphics.paint.SimpleTextPaintable import SimpleTextPaintable
        self.paintable: Paintable = NullPaintable.getInstance()
        self.highScoreCommandsFactory: HighScoreCommandsFactory = HighScoreCommandsFactory.getInstance()
        self.waitPaintable: SimpleTextPaintable = SimpleTextPaintable(self.commonStrings.PLEASE_WAIT_FOR_SERVER, BasicColorFactory.getInstance().WHITE)
        if "highScoresPaintable" not in vars(self): self.highScoresPaintable: HighScoresPaintable = None
        if "highScoresFactoryInterface" not in vars(self): self.highScoresFactoryInterface: HighScoresFactoryInterface = None
        if "colorFillPaintable" not in vars(self): self.colorFillPaintable: ColorFillBasePaintable = None
        self.highScoresHelper: HighScoresHelperBase = HighScoresHelperBase()
        if "gameInfo" not in vars(self): self.gameInfo: GameInfo = None
        if "highScoresCanvasInputProcessor" not in vars(self): self.highScoresCanvasInputProcessor: HighScoresCanvasInputProcessor = None
        self.currentCommand: Command = self.highScoreCommandsFactory.HIGH_SCORE_COMMANDS[0]
        self.hasPainted: bool = False
    

    def __init__(self, commandListener: CommandListener, allBinaryGameLayerManager: AllBinaryGameLayerManager, gameInfo: GameInfo, paintable: HighScoresPaintable, highScoresFactoryInterface: HighScoresFactoryInterface, highScoresCanvasInputProcessorFactoryInterface: HighScoresCanvasInputProcessorFactoryInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.score.displayable.HighScoreRunnable import HighScoreRunnable
        from javax.microedition.lcdui.CommandListener import CommandListener
        from org.allbinary.game.GameInfo import GameInfo
        from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
        from org.allbinary.game.paint.ColorFillPaintableFactory import ColorFillPaintableFactory
        from org.allbinary.game.score.HighScoresCanvasInputProcessorFactoryInterface import HighScoresCanvasInputProcessorFactoryInterface
        from org.allbinary.game.score.HighScoresFactoryInterface import HighScoresFactoryInterface
        from org.allbinary.game.score.HighScoresPaintable import HighScoresPaintable
        from org.allbinary.game.score.NoHighScoresFactory import NoHighScoresFactory
        from org.allbinary.thread.SecondaryThreadPool import SecondaryThreadPool
        super().__init__(commandListener, HighScoresCanvas.NAME, allBinaryGameLayerManager.getBackgroundBasicColor(), allBinaryGameLayerManager.getForegroundBasicColor())
        __class__._init_fields(self)
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.highScoresPaintable = paintable
        self.highScoresFactoryInterface = highScoresFactoryInterface
        self.highScoresCanvasInputProcessor = highScoresCanvasInputProcessorFactoryInterface.getInstance(self)
        self.gameInfo = gameInfo
        self.waitPaintable.setBasicColorP(allBinaryGameLayerManager.getForegroundBasicColor())
        self.getHighScoresPaintable().setBasicColorP(allBinaryGameLayerManager.getForegroundBasicColor())
        self.colorFillPaintable = ColorFillPaintableFactory.getInstance().getInstance(allBinaryGameLayerManager.getBackgroundBasicColor(), False)
        if len(self.highScoresHelper.getHighScoresArray()) == len(NoHighScoresFactory.getInstance().NO_HIGH_SCORES):
            self.setPaintable(self.waitPaintable)
        else:
            self.logUtil.putF("Show HighScores that are already loaded", self, self.commonStrings.CONSTRUCTOR)
            self.updateCommand(self.currentCommand)
            self.setPaintable(self.getHighScoresPaintable())
        SecondaryThreadPool.getInstance().runTask(HighScoreRunnable(self))
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        from javax.microedition.lcdui.CommandListener import CommandListener
        from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
        self.removeAllCommands()
        self.addCommand(GameCommandsFactory.getInstance().CLOSE_AND_SHOW_GAME_CANVAS)
        self.setCommandListener(cmdListener)
    

    def open(self) -> None:
        java_super_call(super(), "open")
        self.highScoresCanvasInputProcessor.open()
    

    # throws Exception
    def close(self) -> None:
        java_super_call(super(), "close")
        self.highScoresCanvasInputProcessor.close()
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.colorFillPaintable.paint(graphics)
        self.paintable.paint(graphics)
        if self.waitPaintable != self.paintable:
            self.highScoresCanvasInputProcessor.paint(graphics)
        java_super_call(super(), "paint", graphics)
        self.hasPainted = True
    

    def executeUpdate(self) -> None:
        try:
            self.highScoresFactoryInterface.fetchHighScores(self.getGameInfo(), self)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.UPDATE, e)
    

    def getHighScoresPaintable(self) -> HighScoresPaintable:
        from org.allbinary.game.score.HighScoresPaintable import HighScoresPaintable
        return self.highScoresPaintable
    

    def setHighScoresArray(self, highScoresArray: list[HighScores]) -> None:
        from org.allbinary.game.score.HighScores import HighScores
        from org.allbinary.logic.string.StringMaker import StringMaker
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
        from javax.microedition.lcdui.Command import Command
        from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
        from org.allbinary.game.score.HighScores import HighScores
        from org.allbinary.game.score.NullHighScoresSingletonFactory import NullHighScoresSingletonFactory
        from org.allbinary.logic.string.StringMaker import StringMaker
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
        java_super_call(super(), "initMenu")
        self.open()
        self.repaintBehavior.onChangeRepaint(self)
    

    def getGameInfo(self) -> GameInfo:
        from org.allbinary.game.GameInfo import GameInfo
        return self.gameInfo
    

    def setPaintable(self, paintable: Paintable) -> None:
        from org.allbinary.graphics.paint.Paintable import Paintable
        self.paintable = paintable
        self.repaintBehavior.onChangeRepaint(self)
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.game.GameInfo import GameInfo
# from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
# from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
# from org.allbinary.game.paint.ColorFillBasePaintable import ColorFillBasePaintable
# from org.allbinary.game.paint.ColorFillPaintableFactory import ColorFillPaintableFactory
# from org.allbinary.game.score.HighScoreCommandsFactory import HighScoreCommandsFactory
# from org.allbinary.game.score.HighScores import HighScores
# from org.allbinary.game.score.HighScoresCanvasInputProcessor import HighScoresCanvasInputProcessor
# from org.allbinary.game.score.HighScoresCanvasInputProcessorFactoryInterface import HighScoresCanvasInputProcessorFactoryInterface
# from org.allbinary.game.score.HighScoresFactoryInterface import HighScoresFactoryInterface
# from org.allbinary.game.score.HighScoresHelperBase import HighScoresHelperBase
# from org.allbinary.game.score.HighScoresPaintable import HighScoresPaintable
# from org.allbinary.game.score.NoHighScoresFactory import NoHighScoresFactory
# from org.allbinary.game.score.NullHighScoresSingletonFactory import NullHighScoresSingletonFactory
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.graphics.paint.NullPaintable import NullPaintable
# from org.allbinary.graphics.paint.Paintable import Paintable
# from org.allbinary.graphics.paint.SimpleTextPaintable import SimpleTextPaintable
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.thread.SecondaryThreadPool import SecondaryThreadPool


