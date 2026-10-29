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

from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
from org.allbinary.graphics.displayable.event.DisplayChangeEventListener import DisplayChangeEventListener
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.game.displayable.canvas.MenuListener import MenuListener


class GameCommandCanvas(MyCanvas, MenuListener, DisplayChangeEventListener, UpdateMyFontInterface):
    id: int = 0

    def _init_fields(self) -> None:
        self.repaintProcessor: Processor = ScreenRepaintProcessorFactory.getInstance().create(self)
        self.gameInputStrings: GameInputStrings = GameInputStrings.getInstance()
        self.foregroundBasicColor: BasicColor = None
        self.backgroundBasicColor: BasicColor = None
        self.inputToGameKeyMapping: InputToGameKeyMapping = PlatformInputMappingFactory.getInstance().getPersistentInputMappingInstance().getInputMapping()
        self.gameKeyFactory: GameKeyFactory = GameKeyFactory.getInstance()
        self.gameKeyEventFactory: GameKeyEventFactory = GameKeyEventFactory.getInstance()
        self.downGameKeyEventHandler: DownGameKeyEventHandler = DownGameKeyEventHandler.getInstance()
        self.upGameKeyEventHandler: UpGameKeyEventHandler = UpGameKeyEventHandler.getInstance()
        self.repaintBehavior: RepaintBehavior = None
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
        self.foregroundColor: int = None
        self.backgroundColor: int = None
        self.menuInputProcessor: BasicMenuInputProcessor = NoMenuInputProcessor.getInstance()
        self.menuPaintable: Paintable = NullPaintable.getInstance()
        self.menuForm: PaintableForm = PaintableForm.getNullPaintableForm()
        self.isSingleKeyRepeatableProcessing: bool = Features.getInstance().isFeature(InputFeatureFactory.getInstance().SINGLE_KEY_REPEAT_PRESS)
        self.fontHeight: int = 0
    

    def __init__(self, cmdListener: CommandListener, name: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(name, CanvasStrings.getInstance().EMPTY_CHILD_NAME_LIST)
        self._init_fields()
        self.repaintBehavior = RepaintBehavior.getInstance()
        self.foregroundBasicColor = foregroundBasicColor
        self.backgroundBasicColor = backgroundBasicColor
        self.foregroundColor = int(self.foregroundBasicColor)
        self.backgroundColor = int(self.backgroundBasicColor)
        self.initCommands(cmdListener)
        if cmdListener != NullCommandListener.NULL_COMMAND_LISTENER:
            try:
                self.initMenu()
                self.repaintProcessor.process()
            except Exception as e:
                raise RuntimeError()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        try:
            font: Font = graphics.getFont()
            self.logUtil.putF(str(StringMaker().append(self.commonStrings.START).append(self.canvasStrings.FD_WIDTH).appendint(int(MyFontProcessor.defaultCharWidth(font))).append(self.canvasStrings.FD_HEIGHT).appendint(int(font.getHeight()))), self, self.canvasStrings.UPDATE_MEASUREMENT)
            self.fontHeight = font.getHeight()
            rectangle: Rectangle = self.createRectangle(self.menuForm.size())
            self.menuForm.init(rectangle, FormTypeFactory.getInstance().VERTICAL_CENTER_FORM)
            self.update()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.canvasStrings.ON_DISPLAY_CHANGE_EVENT, e)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onDisplayChangeEvent(self, displayChangeEvent: DisplayChangeEvent) -> None:
        self.logUtil.putF(str(StringMaker().append(self.commonStrings.START).append(str(DisplayInfoSingleton.getInstance()))), self, self.canvasStrings.ON_DISPLAY_CHANGE_EVENT)
        self.myFontProcessor = self.updateMyFontProcessor
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        self.removeAllCommands()
        self.addCommand(GameCommandsFactory.getInstance().CLOSE_AND_SHOW_GAME_CANVAS)
        self.setCommandListener(cmdListener)
    

    # throws Exception
    def initMenu(self) -> None:
        from org.allbinary.game.displayable.canvas.ImmediateCommandFormInputProcessor import ImmediateCommandFormInputProcessor
        form: ScrollSelectionForm = self.createForm()
        self.menuForm = form
        if form != ScrollSelectionFormNoneFactory.getInstance():
            self.setMenuInputProcessor(ImmediateCommandFormInputProcessor(BasicArrayListD(), -1, self, form))
            self.menuPaintable = FormPaintable(form)
        self.repaintBehavior.onChangeRepaint(self)
    

    # throws Exception
    def createForm(self) -> ScrollSelectionForm:
        items: list[ABCustomItem] = CommandTextItemArrayFactory(AllCommandsVisitor()).getInstance(self.getCommandStack(), self.backgroundBasicColor, self.foregroundBasicColor)
        rectangle: Rectangle = self.createRectangle(len(items))
        return CommandCurrentSelectionFormFactory.getInstance(StringUtil.getInstance().EMPTY_STRING, items, rectangle, FormTypeFactory.getInstance().VERTICAL_CENTER_FORM, 15, False, self.backgroundBasicColor, self.foregroundBasicColor)
    

    def createRectangle(self, size: int) -> Rectangle:
        height: int = size * self.fontHeight
        startY: int = (self.displayInfo.getLastHeight() * 2 / 3) - height
        pointFactory: PointFactory = PointFactory.getInstance()
        rectangle: Rectangle = Rectangle(pointFactory.createXY(30, startY), self.displayInfo.getLastWidth() - 30, startY)
        return rectangle
    

    def open(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "open")
        BasicMotionGesturesHandler.getInstance().addListenerInterface(self.getMenuInputProcessor())
        GameKeyEventHandler.getInstance().addListener(self.getMenuInputProcessor())
        DisplayChangeEventHandler.getInstance().addListenerInterface(self)
    

    # throws Exception
    def close(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CLOSE)
        BasicMotionGesturesHandler.getInstance().removeListener(self.getMenuInputProcessor())
        GameKeyEventHandler.getInstance().removeListener(self.getMenuInputProcessor())
        DisplayChangeEventHandler.getInstance().removeListener(self)
    

    # throws Exception
    def update(self) -> None:
        self.repaintProcessor.process()
    

    def getSourceId(self) -> int:
        return GameCommandCanvas.id
    

    def keyPressed(self, keyCode: int) -> None:
        self.keyPressedByDevice(keyCode, 0)
    

    def keyReleased(self, keyCode: int) -> None:
        self.keyReleasedByDevice(keyCode, 0)
    

    def keyRepeated(self, keyCode: int) -> None:
        self.keyRepeatedByDevice(keyCode, 0)
    

    def keyPressedByDevice(self, keyCode: int, deviceId: int) -> None:
        self.logUtil.putF(str(StringMaker().append(CommonSeps.getInstance().SPACE).appendint(keyCode)), self, self.gameInputStrings.KEY_PRESSED)
        self.addGameKeyEvent(keyCode, 0, False)
    

    def keyReleasedByDevice(self, keyCode: int, deviceId: int) -> None:
        self.removeGameKeyEvent(keyCode, deviceId, False)
    

    def keyRepeatedByDevice(self, keyCode: int, deviceId: int) -> None:
        if self.isSingleKeyRepeatableProcessing:
            self.addGameKeyEvent(keyCode, deviceId, True)
    

    def addGameKeyEvent(self, keyCode: int, deviceId: int, repeated: bool) -> None:
        try:
            gameKey: GameKey = self.inputToGameKeyMapping.getInstanceForCanvas(self, keyCode)
            if gameKey != self.gameKeyFactory.NONE:
                gameKeyEvent: GameKeyEvent = self.gameKeyEventFactory.getInstanceForInput(self, gameKey)
                self.downGameKeyEventHandler.fireEvent(gameKeyEvent)
                self.downGameKeyEventHandler.getInstanceForDevice(deviceId).fireEvent(gameKeyEvent)
            else:
                self.logUtil.putF(str(StringMaker().append(self.gameInputStrings.NO_KEY).appendint(keyCode)), self, self.gameInputStrings.ADD_KEY_EVENT)
        except Exception as e:
            self.logUtil.put("Key Event Error", self, self.gameInputStrings.ADD_KEY_EVENT, e)
    

    def removeGameKeyEvent(self, keyCode: int, deviceId: int, repeated: bool) -> None:
        try:
            gameKey: GameKey = self.inputToGameKeyMapping.getInstanceForCanvas(self, keyCode)
            if gameKey != self.gameKeyFactory.NONE:
                gameKeyEvent: GameKeyEvent = self.gameKeyEventFactory.getInstanceForInput(self, gameKey)
                self.upGameKeyEventHandler.fireEvent(gameKeyEvent)
                self.upGameKeyEventHandler.getInstanceForDevice(deviceId).fireEvent(gameKeyEvent)
            else:
                self.logUtil.putF(str(StringMaker().append(self.gameInputStrings.NO_KEY).appendint(keyCode)), self, self.gameInputStrings.REMOVE_KEY_EVENT)
        except Exception as e:
            self.logUtil.put("Key Event Error", self, self.gameInputStrings.REMOVE_KEY_EVENT, e)
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        self.menuPaintable.paint(graphics)
        self.repaintBehavior.repaint(self)
    

    def setMenuInputProcessor(self, menuInputProcessor: BasicMenuInputProcessor) -> None:
        self.menuInputProcessor = menuInputProcessor
    

    def getMenuInputProcessor(self) -> BasicMenuInputProcessor:
        return self.menuInputProcessor
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.NullCommandListener import NullCommandListener
from org.allbinary.canvas.Processor import Processor
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.InputFeatureFactory import InputFeatureFactory
from org.allbinary.game.displayable.RepaintBehavior import RepaintBehavior
from org.allbinary.game.input.GameInputStrings import GameInputStrings
from org.allbinary.game.input.GameKey import GameKey
from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
from org.allbinary.game.input.event.DownGameKeyEventHandler import DownGameKeyEventHandler
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
from org.allbinary.game.input.event.GameKeyEventHandler import GameKeyEventHandler
from org.allbinary.game.input.event.UpGameKeyEventHandler import UpGameKeyEventHandler
from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent
from org.allbinary.graphics.displayable.event.DisplayChangeEventHandler import DisplayChangeEventHandler
from org.allbinary.graphics.displayable.screen.ScreenRepaintProcessorFactory import ScreenRepaintProcessorFactory
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.graphics.form.CommandCurrentSelectionFormFactory import CommandCurrentSelectionFormFactory
from org.allbinary.graphics.form.FormPaintable import FormPaintable
from org.allbinary.graphics.form.FormTypeFactory import FormTypeFactory
from org.allbinary.graphics.form.PaintableForm import PaintableForm
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
from org.allbinary.graphics.form.ScrollSelectionFormNoneFactory import ScrollSelectionFormNoneFactory
from org.allbinary.graphics.form.item.CommandTextItemArrayFactory import CommandTextItemArrayFactory
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.graphics.form.item.validation.AllCommandsVisitor import AllCommandsVisitor
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.input.motion.gesture.observer.BasicMotionGesturesHandler import BasicMotionGesturesHandler
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.game.displayable.canvas.NoMenuInputProcessor import NoMenuInputProcessor


