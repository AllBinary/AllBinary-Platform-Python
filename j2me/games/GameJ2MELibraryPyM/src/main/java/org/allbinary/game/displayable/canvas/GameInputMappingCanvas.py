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

# from javax.microedition.lcdui.Command import Command
from org.allbinary.game.input.mapping.InputMappingInterface import InputMappingInterface
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.game.displayable.canvas.GameCommandCanvas import GameCommandCanvas


class GameInputMappingCanvas(GameCommandCanvas, InputMappingInterface):
    NAME: str = "GameInputMappingCanvas"
    DISPLAY: Command = Command("Controls", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 2)
    DEFAULT: Command = Command("Default", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 2)

    def _init_fields(self) -> None:
        self.paintable: ProcessPaintable = None
        self.helpPaintable: InputMappingHelpPaintable = None
        self.colorFillPaintable: ColorFillBasePaintable = None
        self.inputMapping: PersistentInputMapping = None
        self.NONE: GameKey = GameKeyFactory.getInstance().NONE
        self.abeClientInformation: AbeClientInformationInterface = None
        self.selectedGameKey: GameKey = self.NONE
        self.selectedInput: Input = self.NONE
        self.inputFactory: InputFactory = InputFactory.getInstance()
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, commandListener: CommandListener, allBinaryGameLayerManager: AllBinaryGameLayerManager, helpPaintable: HelpPaintable) -> None:
        super().__init__(commandListener, GameInputMappingCanvas.NAME, allBinaryGameLayerManager.getBackgroundBasicColor(), allBinaryGameLayerManager.getForegroundBasicColor())
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        if helpPaintable is None:
            raise Exception("Help Paintable Exception")
        self.abeClientInformation = abeClientInformation
        self.helpPaintable = helpPaintable
        self.inputMapping = PlatformInputMappingFactory.getInstance().getPersistentInputMappingInstance()
        self.paintable = ProcessPaintable()
        self.colorFillPaintable = ColorFillPaintableFactory.getInstance().getInstance(allBinaryGameLayerManager.getBackgroundBasicColor(), False)
    

    # throws Exception
    def close(self) -> None:
        super().close()
        self.paintable.process()
        self.selectedGameKey = self.NONE
        self.selectedInput = self.NONE
        self.update()
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        from org.allbinary.game.displayable.canvas.GameInputMappingInstructionsCanvas import GameInputMappingInstructionsCanvas
        self.removeAllCommands()
        self.addCommand(GameCommandsFactory.getInstance().CLOSE_AND_SHOW_GAME_CANVAS)
        self.addCommand(GameInputMappingCanvas.DEFAULT)
        self.addCommand(GameInputMappingInstructionsCanvas.DISPLAY)
        self.setCommandListener(cmdListener)
    

    def keyPressed(self, keyCode: int) -> None:
        self.keyPressedByDevice(keyCode, 0)
    

    def keyReleased(self, keyCode: int) -> None:
        self.keyReleasedByDevice(keyCode, 0)
    

    def keyRepeated(self, keyCode: int) -> None:
        self.keyRepeatedByDevice(keyCode, 0)
    

    def keyPressedByDevice(self, keyCode: int, deviceId: int) -> None:
        self.addGameKey(keyCode, False)
        super().keyPressedByDevice(keyCode, 0)
    

    def addGameKey(self, keyCode: int, repeated: bool) -> None:
        try:
            self.logUtil.putF(str(StringMaker().append("Raw Device Key Code: ").append(format(keyCode, "x"))), self, self.gameInputStrings.ADD_KEY_EVENT)
            gameKey: GameKey = self.inputToGameKeyMapping.getInstanceForCanvas(self, keyCode)
            input: Input = self.inputFactory.getInstanceById(keyCode)
            self.processInputMapping(gameKey, input)
        except Exception as e:
            self.logUtil.put("Key Event Error", self, self.gameInputStrings.ADD_KEY_EVENT, e)
    

    # throws Exception
    def processInputMapping(self, gameKey: GameKey, input: Input) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Start Passed GameKey: ")
        stringBuffer.append(self.stringUtil.toString(gameKey))
        stringBuffer.append(" Input: ")
        stringBuffer.append(self.stringUtil.toString(input))
        self.logUtil.putF(str(stringBuffer), self, self.commonStrings.PROCESS)
        if self.selectedGameKey != self.NONE:
            self.gameActionCrud(gameKey, input)
        else:
            self.setSelectedAction(gameKey)
    

    def setSelectedAction(self, gameKey: GameKey) -> None:
        self.logUtil.putF(str(StringMaker().append("Selected GameKey: ").append(self.stringUtil.toString(gameKey))), self, "setSelectedAction")
        self.selectedGameKey = gameKey
        self.selectedInput = self.NONE
        self.helpPaintable.update(self.selectedGameKey, self.selectedInput)
        self.repaintBehavior.onChangeRepaint(self)
    

    # throws Exception
    def gameActionCrud(self, gameKey: GameKey, input: Input) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Start GameKey: ")
        stringBuffer.append(self.stringUtil.toString(self.selectedGameKey))
        stringBuffer.append(" Input: ")
        stringBuffer.append(self.stringUtil.toString(self.selectedInput))
        self.logUtil.putF(str(stringBuffer), self, "gameActionCrud")
        if self.selectedInput == self.NONE:
            list_: BasicArrayList = self.inputMapping.getInputMapping().getMappedInput(self.selectedGameKey)
            isInputAlreadyMappedToSelectedAction: bool = list_.contains(input)
            if isInputAlreadyMappedToSelectedAction:
                self.logUtil.putF(str(StringMaker().append("Already Mapped Input: ").append(self.stringUtil.toString(input))), self, "gameActionCrud")
                self.selectedInput = input
                self.helpPaintable.update(self.selectedGameKey, self.selectedInput)
                self.repaintBehavior.onChangeRepaint(self)
            else:
                self.addNewMapping(gameKey, input)
        elif self.inputMapping.isDelete(input):
            self.deleteCurrentMapping()
        else:
            self.setSelectedAction(gameKey)
    

    # throws Exception
    def addNewMapping(self, gameKey: GameKey, input: Input) -> None:
        METHOD_NAME: str = "addNewMapping"
        self.logUtil.putF(self.commonStrings.START, self, METHOD_NAME)
        isInputAlreadyMapped: bool = self.inputMapping.getInputMapping().isMapped(input)
        if not isInputAlreadyMapped and not self.inputMapping.isSystemInput(input):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Add Key Mapping : GameKey: ")
            stringBuffer.append(self.stringUtil.toString(self.selectedGameKey))
            stringBuffer.append(" Input: ")
            stringBuffer.append(self.stringUtil.toString(self.selectedInput))
            self.logUtil.putF(str(stringBuffer), self, METHOD_NAME)
            self.inputMapping.getInputMapping().add(self.selectedGameKey, input)
            self.selectedInput = input
            self.update()
        else:
            self.logUtil.putF("Unable to add Mapping since one already exists or is MENU, HOME, or BACK key and setting selected action to what it is already mapped to", self, METHOD_NAME)
            self.setSelectedAction(gameKey)
    

    # throws Exception
    def deleteCurrentMapping(self) -> None:
        METHOD_NAME: str = "deleteCurrentMapping"
        list_: BasicArrayList = self.inputMapping.getInputMapping().getMappedInput(self.selectedGameKey)
        if list_.size() > 1:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Start GameKey: ")
            stringBuffer.append("Remove Key Mapping: GameKey: ")
            stringBuffer.append(self.stringUtil.toString(self.selectedGameKey))
            stringBuffer.append(" Input: ")
            stringBuffer.append(self.stringUtil.toString(self.selectedInput))
            self.logUtil.putF(str(stringBuffer), self, METHOD_NAME)
            self.inputMapping.getInputMapping().remove(self.selectedGameKey, self.selectedInput)
            self.selectedInput = self.NONE
            self.update()
        else:
            self.logUtil.putF("Can't Remove Last Key Mapping", self, METHOD_NAME)
    

    # throws Exception
    def setDefault(self) -> None:
        self.inputMapping.setDefault(self.abeClientInformation)
        self.helpPaintable.update(self.NONE, self.NONE)
        self.repaintBehavior.onChangeRepaint(self)
    

    # throws Exception
    def update(self) -> None:
        self.inputMapping.update(self.abeClientInformation)
        self.helpPaintable.update(self.selectedGameKey, self.selectedInput)
        self.repaintBehavior.onChangeRepaint(self)
    

    def paint(self, graphics: Graphics) -> None:
        self.colorFillPaintable.paint(graphics)
        self.helpPaintable.paint(graphics)
        self.paintable.paint(graphics)
        super().paint(graphics)
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.game.input.GameKey import GameKey
from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
from org.allbinary.game.input.Input import Input
from org.allbinary.game.input.InputFactory import InputFactory
from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
from org.allbinary.game.input.mapping.PersistentInputMapping import PersistentInputMapping
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.paint.ColorFillBasePaintable import ColorFillBasePaintable
from org.allbinary.game.paint.ColorFillPaintableFactory import ColorFillPaintableFactory
from org.allbinary.game.paint.help.HelpPaintable import HelpPaintable
from org.allbinary.game.paint.help.InputMappingHelpPaintable import InputMappingHelpPaintable
from org.allbinary.graphics.paint.ProcessPaintable import ProcessPaintable
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.util.BasicArrayList import BasicArrayList


