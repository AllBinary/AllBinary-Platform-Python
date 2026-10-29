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


class GameOptionsForm(CommandForm):

    def _init_fields(self) -> None:
        self.meUtil: MEUtil = MEUtil.getInstance()
    

    def __init__(self, commandListener: CommandListener, title: str, backgrounBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(commandListener, title, backgrounBasicColor, foregroundBasicColor)
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.addConfiguration()
        gameFeatureFormUtil: GameFeatureFormUtil = GameFeatureFormUtil.getInstance()
        gameFeatureFormUtil.addChoiceGroup(self, GameFeatureChoiceGroups.getExclusiveInstance().get(), Choice.EXCLUSIVE)
        gameFeatureFormUtil.addChoiceGroup(self, GameFeatureChoiceGroups.getMultipleInstance().get(), Choice.MULTIPLE)
        self.initCommands(commandListener)
        self.setItemStateListener(GameFeatureItemStateListener(self))
        self.addTextFieldsIfSimulated()
    

    # throws Exception
    def closeClientInformation(self, abeClientInformation: AbeClientInformationInterface) -> None:
        super().close()
        self.save(abeClientInformation)
    

    def addTextFieldsIfSimulated(self) -> None:
        key: str = OrientationData.getInstance().ORIENTATION_SENSOR_INPUT
        hashtable: ABHashtable[object, object] = GameFeatureChoiceGroups.getExclusiveInstance().get()
        if hashtable is not None:
            listCanBeNull: object = hashtable.get(key)
            if listCanBeNull is not None:
                list_: BasicArrayList = listCanBeNull
                if list_.contains(SensorFeatureFactory.getInstance().SIMULATED_ORIENTATION_SENSORS):
                    self.addTextFields()
    

    def addTextFields(self) -> None:
        from org.allbinary.game.configuration.GameConfigurationTextInput import GameConfigurationTextInput
        hashtable: ABHashtable[object, object] = GameConfigurationTextInput.getHashtable()
        size: int = hashtable.size()
        objectArray: list[object] = HashtableUtil.getInstance().getKeysAsArray(hashtable)
        gameConfigurationTextInput: GameConfigurationTextInput = None
        textField: TextField = None
        for index in range(0, size):
            gameConfigurationTextInput = hashtable.get(objectArray[index])
            textField = TextField(gameConfigurationTextInput.getLabel(), gameConfigurationTextInput.getText(), 30, TextField.ANY)
            self.meUtil.appendItem(self, textField)
    

    def addConfiguration(self) -> None:
        from org.allbinary.game.configuration.GameConfigurationSingleton import GameConfigurationSingleton
        from org.allbinary.game.configuration.GameConfigurationGauge import GameConfigurationGauge
        METHOD_NAME: str = "addConfiguration"
        NAME: str = "Name: "
        list_: BasicArrayList = GameConfigurationSingleton.getInstance().getOptionsBasicArrayList()
        GAUGE_CHANGE: Command = MyCommandsFactory.getInstance().GAUGE_CHANGE
        stringMaker: StringMaker = StringMaker()
        size: int = list_.size()
        gameConfiguration: GameConfiguration = None
        gauge: GameConfigurationGauge = None
        for index in range(0, size):
            gameConfiguration = list_.objectArray[index]
            stringMaker.delete(0, stringMaker.length())
            self.logUtil.putF(str(stringMaker.append(NAME).append(str(gameConfiguration))), self, METHOD_NAME)
            gauge = GameConfigurationGauge(gameConfiguration)
            gauge.setDefaultCommand(GAUGE_CHANGE)
            gauge.setItemCommandListener(GameFeatureItemCommandListener(self))
            self.meUtil.appendItem(self, gauge)
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        gameCommandsFactory: GameCommandsFactory = GameCommandsFactory.getInstance()
        self.removeAllCommands()
        self.addCommand(gameCommandsFactory.CLOSE_OPTIONS)
        self.addCommand(gameCommandsFactory.DEFAULT_OPTIONS)
        self.setCommandListener(cmdListener)
    

    # throws Exception
    def save(self, abeClientInformation: AbeClientInformationInterface) -> None:
        from org.allbinary.game.configuration.GameConfigurationTextInput import GameConfigurationTextInput
        from org.allbinary.game.configuration.GameConfigurationUtil import GameConfigurationUtil
        from org.allbinary.game.configuration.GameConfigurationUtil import GameConfigurationUtil
        from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
        from org.allbinary.game.configuration.SCALE import SCALE
        from org.allbinary.game.configuration.SCALE import SCALE
        size: int = self.size()
        item: Item = None
        for index in range(0, size):
            item = self.get(index)
            if isinstance(item, GameConfigurationGauge):
                GameConfigurationUtil.getInstance().update(item)
            elif isinstance(item, TextField):
                GameConfigurationTextInput.update(item)
        GameConfigurationUtil.getInstance().updateCompetitionValue()
        hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        SCALE: GameConfiguration = GameConfigurationCentral.getInstance().SCALE
        hashtable.put(SCALE.getName(), str(SCALE.getValue()))
        keyValuePersistance: KeyValuePersistance = GameConfigurationPersistanceSingleton.getInstance()
        keyValuePersistance.clear()
        keyValuePersistance.loadAll(abeClientInformation)
        list_: BasicArrayList = keyValuePersistance.getIds()
        keyValuePersistance.save(abeClientInformation, hashtable)
        size2: int = list_.size()
        integer: int = None
        for index in range(0, size2):
            integer = list_.objectArray[index]
            keyValuePersistance.delete(abeClientInformation, int(integer))
# from javax.microedition.lcdui.Choice import Choice
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Item import Item
# from javax.microedition.lcdui.TextField import TextField
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.game.configuration.feature.GameFeatureChoiceGroups import GameFeatureChoiceGroups
from org.allbinary.game.configuration.feature.GameFeatureFormUtil import GameFeatureFormUtil
from org.allbinary.game.configuration.feature.GameFeatureItemCommandListener import GameFeatureItemCommandListener
from org.allbinary.game.configuration.feature.GameFeatureItemStateListener import GameFeatureItemStateListener
from org.allbinary.game.configuration.feature.SensorFeatureFactory import SensorFeatureFactory
from org.allbinary.game.configuration.persistance.GameConfigurationPersistanceSingleton import GameConfigurationPersistanceSingleton
from org.allbinary.game.configuration.persistance.KeyValuePersistance import KeyValuePersistance
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.displayable.command.MyCommandsFactory import MyCommandsFactory
from org.allbinary.input.gyro.OrientationData import OrientationData
from org.allbinary.logic.MEUtil import MEUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.HashtableUtil import HashtableUtil
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable


