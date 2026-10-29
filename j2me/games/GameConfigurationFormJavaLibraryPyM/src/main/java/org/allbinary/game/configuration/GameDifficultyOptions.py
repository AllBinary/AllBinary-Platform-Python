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
# package org.allbinary.game.configuration

from __future__ import annotations

from org.allbinary.graphics.displayable.screen.CommandForm import CommandForm


class GameDifficultyOptions(CommandForm):

    def _init_fields(self) -> None:
        self.meUtil: MEUtil = MEUtil.getInstance()
        self.list_: BasicArrayList = None
    

    def __init__(self, commandListener: CommandListener, title: str, list_: BasicArrayList, backgrounBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(commandListener, title, backgrounBasicColor, foregroundBasicColor)
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.list_ = list_
        self.update()
        self.initCommands(commandListener)
        gameDifficultyFactory: GameDifficultyFactory = GameDifficultyFactory.getInstance()
        self.setSelectedId(gameDifficultyFactory.getLevel())
    

    def open(self) -> None:
        super().open()
    

    # throws Exception
    def close(self) -> None:
        super().close()
        self.save()
    

    # throws Exception
    def save(self) -> None:
        gameDifficultyFactory: GameDifficultyFactory = GameDifficultyFactory.getInstance()
        gameDifficultyFactory.setLevel(self.getSelectedId())
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        gameCommandsFactory: GameCommandsFactory = GameCommandsFactory.getInstance()
        self.removeAllCommands()
        self.addCommand(gameCommandsFactory.CLOSE_AND_SHOW_GAME_CANVAS)
        self.setCommandListener(cmdListener)
    

    # throws Exception
    def update(self) -> None:
        self.deleteAll()
        self.add(self.list_, "Difficulty", Choice.EXCLUSIVE)
        super().update()
    

    def add(self, list_: BasicArrayList, name: str, option: int) -> None:
        choiceGroup: ChoiceGroup = self.getChoiceGroup(list_, name, option)
        if list_.size() > 0:
            choiceGroup.setSelectedIndex(0, True)
        self.meUtil.appendItem(self, choiceGroup)
    

    def getChoiceGroup(self, list_: BasicArrayList, name: str, option: int) -> ChoiceGroup:
        METHOD_NAME: str = "addChoiceGroup"
        NAME: str = "Adding Choice: "
        choiceGroup: ChoiceGroup = ChoiceGroup(name, option, StringUtil.getInstance().getArrayInstance(), NullImage.NULL_IMAGE_ARRAY)
        size: int = list_.size()
        anyType: object = None
        for index in range(0, size):
            anyType = list_.objectArray[index]
            self.logUtil.putF(str(StringMaker().append(NAME).append(str(anyType))), self, METHOD_NAME)
            choiceGroup.append(str(anyType), NullImage.NULL_IMAGE)
        return choiceGroup
    

    def setSelectedId(self, id: int) -> None:
        choiceGroup: ChoiceGroup = self.get(0)
        choiceGroup.setSelectedIndex(id, True)
    

    def getSelectedId(self) -> int:
        choiceGroup: ChoiceGroup = self.get(0)
        return choiceGroup.getSelectedIndex()
    

    def getSelectedText(self) -> int:
        choiceGroup: ChoiceGroup = self.get(0)
        value: int = int(str(choiceGroup.getString(choiceGroup.getSelectedIndex())))
        return value
# from javax.microedition.lcdui.Choice import Choice
# from javax.microedition.lcdui.ChoiceGroup import ChoiceGroup
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.game.configuration.persistance.GameDifficultyFactory import GameDifficultyFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.logic.MEUtil import MEUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.BasicArrayList import BasicArrayList


