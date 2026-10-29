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
# package org.allbinary.graphics.canvas.transition.progress

from __future__ import annotations

from org.allbinary.canvas.RunnableCanvas import RunnableCanvas
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface


class ProgressCanvas(RunnableCanvas, PaintableInterface, UpdateMyFontInterface):
    class ProgressPaintable(Paintable):

        def _init_fields(self) -> None:
            self.progressCanvas: ProgressCanvas = None
        

        def __init__(self, progressCanvas: ProgressCanvas) -> None:
            super().__init__()
            self._init_fields()
            self.progressCanvas = progressCanvas
        

        def paint(self, graphics: Graphics) -> None:
            self.progressCanvas.paint2(graphics)

    def _init_fields(self) -> None:
        self.hasPainted: bool = False
        self.backgroundBasicColor: BasicColor = None
        self.GAUGE_PAINTABLE: Paintable = ProgressPaintable(self)
        self.maxValue: float = 100.0
        self.gauge: ABCustomGaugeItem = None
        self.TEXT: str = self.commonStrings.LOADING
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
        self.allbinaryMidlet: AllBinaryMidlet = AllBinaryMidlet.getNullInstance()
        self.value: float = 0.0
        self.text: str = self.TEXT
        self.background: bool = True
        self.paintable: PaintableInterface = self.GAUGE_PAINTABLE
        self.inProgress: bool = False
        self.IN_GAME_PROCESSOR: Processor = (Processor()  # Java anonymous class body:
#         self.pathFindingThreadPool: ThreadPool = PathFindingThreadPool.getInstance()
#         
# 
#         # throws Exception
#         def process(self) -> None:
#             self.pathFindingThreadPool.runAPriorityTask()
)
        self.inGameProcessor: Processor = Processor.getInstance()
        self.progressEndListener: ProgressEndListener = ProgressEndListener.instance
        self.backgroundLabel: str = "Background AI Game Loading..."
        self.START_BACKGROUND: str = "startBackground"
        self.ADD_PORTION: str = "addPortion"
        self.ADD_EARLY_PORTION: str = "addEarlyPortion"
    

    def __init__(self, title: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(NullCommandListener.NULL_COMMAND_LISTENER, CanvasStrings.getInstance().EMPTY_CHILD_NAME_LIST, False)
        self._init_fields()
        self.backgroundBasicColor = backgroundBasicColor
        self.gauge = ABCustomGaugeItem(StringUtil.getInstance().EMPTY_STRING, int(self.maxValue), 0, backgroundBasicColor, foregroundBasicColor)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.gauge.setHeight(font.getHeight() + 2)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def init(self, gameMidlet: AllBinaryMidlet) -> None:
        self.allbinaryMidlet = gameMidlet
    

    # throws Exception
    def update(self, graphics: Graphics) -> None:
        pass
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        pass
    

    def getMaxValue(self) -> float:
        return self.maxValue
    

    def start(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.START_METHOD_NAME)
        self.setBackground(True)
        self.gauge.setHeight(30)
        self.gauge.setLabel(self.commonStrings.PLEASE_WAIT)
        self.setText(self.TEXT)
        self.setValue(0)
        self.inGameProcessor = Processor.getInstance()
        self.paintable = self.GAUGE_PAINTABLE
        self.inProgress = True
    

    def startBackground(self, background: bool) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.START_BACKGROUND)
        self.setBackground(background)
        self.myFontProcessor = self.updateMyFontProcessor
        self.gauge.setLabel(self.backgroundLabel)
        self.setText(self.TEXT)
        self.setValue(0)
        self.inGameProcessor = Processor.getInstance()
        self.paintable = self.GAUGE_PAINTABLE
    

    def endActual(self) -> None:
        self.allbinaryMidlet.commandAction(GameCommandsFactory.getInstance().SHOW_GAME_CANVAS, NullCanvas.NULL_CANVAS)
        self.inProgress = False
        self.inGame()
    

    def inGame(self) -> None:
        self.progressEndListener.onEndEvent()
        self.inGameProcessor = self.IN_GAME_PROCESSOR
    

    def end(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.END_METHOD_NAME)
        self.gauge.setValue(self.getMaxValue())
        self.endActual()
        self.paintable = NullPaintable.getInstance()
    

    def endFromInitialLazyLoadingComplete(self) -> None:
        self.progressEndListener.onEndEvent()
        self.gauge.setValue(self.getMaxValue())
        self.inGameProcessor = self.IN_GAME_PROCESSOR
    

    def isInGame(self) -> bool:
        if self.inGameProcessor == self.IN_GAME_PROCESSOR:
            return True
        return False
    

    def endIfPaintedSinceStart(self) -> None:
        pass
    

    def addEarlyPortion(self, value: int, text: str, index: int) -> None:
        self.setText(str(StringMaker().append(text).append(str(SmallIntegerSingletonFactory.getInstance().getAt(index)))))
        self.gauge.setValue(self.gauge.getValue() + self.getMaxValue() / float(value))
    

    def addPortion(self, value: int, text: str, index: int) -> None:
        self.setText(str(StringMaker().append(text).append(str(SmallIntegerSingletonFactory.getInstance().getAt(index)))))
        PreLogUtil.put(self.text, self, self.ADD_PORTION)
        self.gauge.setValue(self.gauge.getValue() + self.getMaxValue() / float(value))
    

    def addNormalPortion(self, value: int, text: str) -> None:
        if self.text != text:
            PreLogUtil.put(text, self, self.ADD_PORTION)
        self.setText(text)
        self.gauge.setValue(self.gauge.getValue() + self.getMaxValue() / float(value))
    

    def setValue(self, value: int) -> None:
        self.value = float(value)
        self.gauge.setValue(float(value))
    

    def paint(self, graphics: Graphics) -> None:
        self.paintable.paint(graphics)
    

    def paint2(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        graphics.setColor(int(self.backgroundBasicColor))
        graphics.fillRect(0, 0, self.displayInfo.getLastWidth(), self.displayInfo.getLastHeight())
        self.gauge.paintXY(graphics, 0, 0)
        self.hasPainted = True
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
    

    def getValue(self) -> float:
        return self.value
    

    def setText(self, text: str) -> None:
        self.text = text
    

    def getText(self) -> str:
        return self.text
    

    def setBackground(self, background: bool) -> None:
        self.background = background
    

    def isBackground(self) -> bool:
        return self.background
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.NullCanvas import NullCanvas
# from javax.microedition.lcdui.NullCommandListener import NullCommandListener
from org.allbinary.canvas.Processor import Processor
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.graphics.form.item.ABCustomGaugeItem import ABCustomGaugeItem
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.midlet.AllBinaryMidlet import AllBinaryMidlet
from org.allbinary.thread.PathFindingThreadPool import PathFindingThreadPool
from org.allbinary.thread.ThreadPool import ThreadPool
from org.allbinary.graphics.canvas.transition.progress.ProgressPaintable import ProgressPaintable
from org.allbinary.graphics.canvas.transition.progress.ProgressEndListener import ProgressEndListener


